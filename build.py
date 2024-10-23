import subprocess
from pathlib import Path

def build(context) -> None:
    """Generate protobuf files during package build"""
    root = Path(__file__).parent
    proto_dir = root / "src" / "chatbot_proto" / "protos"
    output_dir = root / "src" / "chatbot_proto"
    proto_file = proto_dir / "search.proto"
    
    subprocess.run([
        "python", "-m", "grpc_tools.protoc",
        f"--proto_path={proto_dir}",
        f"--python_out={output_dir}",
        f"--grpc_python_out={output_dir}",
        proto_file
    ], check=True)
