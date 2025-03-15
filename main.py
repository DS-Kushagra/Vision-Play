from utils import read_video, save_video
from trackers import Tracker
import cv2
from team_assigner import TeamAssigner

def main():
    # Read video frames
    video_frames = read_video('Input-Videos/08fd33_4.mp4')

    # Initialize tracker
    tracker = Tracker("models/best.pt")

    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path="stubs/tracks_stubs.pkl")

    # Interpolate ball positions
    tracks["ball"] = tracker.interpolate_ball_position(tracks["ball"])
    
    # Assign player teams
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], tracks['players'][0])

    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, player_track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num], player_track["bbox"], player_id)
            tracks["players"][frame_num][player_id]["team"] = team
            tracks["players"][frame_num][player_id]["team_color"] = team_assigner.team_colors[team]

    # Draw object tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks)

    # Save video
    save_video(output_video_frames, 'Output-Videos/output_video.avi')

if __name__ == "__main__":
    main()