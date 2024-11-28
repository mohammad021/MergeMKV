import os
import subprocess
import sys
import shutil
from tqdm import tqdm


def install_package(package):
    """Installs a Python package using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def check_ffmpeg(default_path=None):
    """Checks if ffmpeg is installed, and sets up the path if not."""
    if not shutil.which("ffmpeg"):
        print("ffmpeg not found. Please provide the root path of ffmpeg installation or press Enter to use the default path:")
        ffmpeg_path = input().strip()

        if not ffmpeg_path and default_path:
            ffmpeg_path = default_path

        if os.path.exists(ffmpeg_path):
            os.environ["PATH"] += os.pathsep + os.path.join(ffmpeg_path, "bin")
        else:
            print("Invalid path provided. Please make sure the path is correct and try again.")
            sys.exit(1)


# Default path for ffmpeg
default_ffmpeg_path = "C:\\ffmpeg"  # Set your default path here

# Check if ffmpeg is installed
check_ffmpeg(default_ffmpeg_path)

# Check and install required libraries
try:
    import ffmpeg
except ImportError:
    install_package("ffmpeg-python")
    import ffmpeg

# Install tqdm for progress bar
try:
    from tqdm import tqdm
except ImportError:
    install_package("tqdm")
    from tqdm import tqdm


def merge_files(audio_path, video_path, output_path):
    """
    Merges an audio file into a video file to create a new output file.
    """
    command = [
        'ffmpeg',
        '-i', video_path,
        '-i', audio_path,
        '-c', 'copy',
        '-map', '0:v',
        '-map', '1:a',
        '-shortest', output_path
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        return f"Error merging files: {result.stderr}"
    return f"Successfully merged {video_path} and {audio_path} into {output_path}"


def main():
    """
    Main function to process video files in the current directory and merge
    them with corresponding audio files.
    """
    source_folder = os.getcwd()  # Use current working directory
    output_folder = os.path.join(source_folder, 'mkv')  # Create output folder in the same directory

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    supported_formats = [".mp4", ".mkv"]  # Supported formats
    files_to_process = [
        file for file in os.listdir(source_folder)
        if any(file.endswith(ext) for ext in supported_formats)
    ]

    if not files_to_process:
        print("No supported video files found.")
        return

    print(f"Found {len(files_to_process)} video files to process.")

    # Process files with a progress bar
    for file in tqdm(files_to_process, desc="Processing files", unit="file"):
        video_file = os.path.join(source_folder, file)
        audio_file = os.path.join(source_folder, file.rsplit('.', 1)[0] + ".mp3")  # Assuming audio files are in mp3 format

        if os.path.exists(audio_file):
            output_file = os.path.join(output_folder, file.rsplit('.', 1)[0] + ".mkv")
            message = merge_files(audio_file, video_file, output_file)
            tqdm.write(message)  # Print the message without breaking the progress bar
        else:
            tqdm.write(f"No matching audio file for {file}")


if __name__ == "__main__":
    main()
