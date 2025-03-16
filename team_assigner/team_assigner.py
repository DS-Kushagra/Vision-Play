from sklearn.cluster import KMeans
import numpy as np  # Import numpy for array manipulation

class TeamAssigner():
    def __init__(self):
        self.team_colors = {}
        self.player_team_dict = {}
        self.kmeans = None  # Initialize kmeans as None

    def get_clutering_model(self, image):
        # Reshape the image into 2D array
        image_2D = image.reshape(-1, 3)
        # Perform K-means clustering
        kmeans = KMeans(n_clusters=2, init="k-means++", n_init=1).fit(image_2D)
        return kmeans

    def get_player_color(self, frame, bbox):
        image = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]

        top_half_image = image[0: int(image.shape[0]/2), :]

        # Get clustering model
        kmeans = self.get_clutering_model(top_half_image)

        # Get cluster labels
        labels = kmeans.labels_

        # Reshape the labels to the original image shape
        clustered_image = labels.reshape(top_half_image.shape[0], top_half_image.shape[1])

        # Get the player cluster
        corner_clusters = [(clustered_image[0, 0], clustered_image[0, -1]), (clustered_image[-1, 0], clustered_image[-1, -1])]
        non_player_cluster = max(set(corner_clusters), key=corner_clusters.count)

        # Determine the player cluster by comparing tuples
        if corner_clusters[0] == non_player_cluster:
            player_cluster = corner_clusters[1]
        else:
            player_cluster = corner_clusters[0]

        #Get the index of the player cluster in the kmeans.cluster_centers_ list.
        player_cluster_index = 0
        if clustered_image[0,0] == player_cluster[0] and clustered_image[0,-1] == player_cluster[1]:
            player_cluster_index = clustered_image[0,0]
        elif clustered_image[-1,0] == player_cluster[0] and clustered_image[-1,-1] == player_cluster[1]:
            player_cluster_index = clustered_image[-1,0]

        # Get the player color
        player_color = kmeans.cluster_centers_[player_cluster_index]

        return player_color

    def assign_team_color(self, frame, player_detections):
        player_colors = []
        for _, player_detection in player_detections.items():
            bbox = player_detection["bbox"]
            player_color = self.get_player_color(frame, bbox)
            player_colors.append(player_color)

        kmeans = KMeans(n_clusters=2, init="k-means++", n_init=10).fit(player_colors)

        self.kmeans = kmeans

        self.team_colors[1] = kmeans.cluster_centers_[0]
        self.team_colors[2] = kmeans.cluster_centers_[1]

    def get_player_team(self, frame, player_bbox, player_id):
        if player_id in self.player_team_dict:
            return self.player_team_dict[player_id]

        player_color = self.get_player_color(frame, player_bbox)

        if self.kmeans is None: #Add check for kmeans existence.
            print("Error: KMeans model has not been trained yet. Call assign_team_color first.")
            return None

        team_id = self.kmeans.predict(player_color.reshape(1, -1))[0]
        team_id += 1

        if player_id == 91:
            team_id = 1

        self.player_team_dict[player_id] = team_id
        return team_id