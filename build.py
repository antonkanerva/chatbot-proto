import subprocess
from pathlib import Path

def build(context) -> None:
    """Generate protobuf files during package build"""
    root = Path(__file__).parent
    src_dir = root / "src"
    proto_dir = src_dir / "chatbot_proto" / "protos"
    output_dir = src_dir / "chatbot_proto"
    proto_file = proto_dir / "search.proto"
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Generating proto files from {proto_file} to {output_dir}")
    result = subprocess.run([
        "python", "-m", "grpc_tools.protoc",
        f"--proto_path={proto_dir}",
        f"--python_out={output_dir}",
        f"--grpc_python_out={output_dir}",
        proto_file
    ], check=True, capture_output=True, text=True)
    
    print(f"Proto generation stdout: {result.stdout}")
    print(f"Proto generation stderr: {result.stderr}")
