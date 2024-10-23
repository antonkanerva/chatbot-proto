import subprocess
from pathlib import Path

def generate_protos():
    # Get the directory containing this script
    root_dir = Path(__file__).parent
    proto_dir = root_dir / "src" / "chatbot_proto" / "protos"
    
    # Create the output directory if it doesn't exist
    proto_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate Python files from proto
    proto_file = proto_dir / "search.proto"
    subprocess.run([
        "python", "-m", "grpc_tools.protoc",
        f"--proto_path={proto_dir}",
        f"--python_out={proto_dir}",
        f"--grpc_python_out={proto_dir}",
        proto_file
    ], check=True)

if __name__ == "__main__":
    generate_protos()