import subprocess
import sys
from pathlib import Path

def generate_protos():
    """Generate protobuf files"""
    root = Path(__file__).parent.parent
    proto_dir = root / "src" / "chatbot_proto" / "protos"
    output_dir = root / "src" / "chatbot_proto"
    proto_file = proto_dir / "search.proto"

    subprocess.run([
        sys.executable, "-m", "grpc_tools.protoc",
        f"--proto_path={proto_dir}",
        f"--python_out={output_dir}",
        f"--grpc_python_out={output_dir}",
        str(proto_file)
    ], check=True)

if __name__ == "__main__":
    generate_protos()
