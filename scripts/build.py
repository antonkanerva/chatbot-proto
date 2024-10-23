import subprocess
import sys
from pathlib import Path


def fix_grpc_imports(file_path: Path) -> None:
    """Fix the import statements in generated grpc files"""
    content = file_path.read_text()
    # Replace local import with package import
    content = content.replace(
        "import search_pb2 as search__pb2", "from . import search_pb2 as search__pb2"
    )
    file_path.write_text(content)


def generate_protos():
    """Generate protobuf files"""
    root = Path(__file__).parent.parent
    proto_dir = root / "src" / "chatbot_proto" / "protos"
    output_dir = root / "src" / "chatbot_proto"
    proto_file = proto_dir / "search.proto"

    subprocess.run(
        [
            sys.executable,
            "-m",
            "grpc_tools.protoc",
            f"--proto_path={proto_dir}",
            f"--python_out={output_dir}",
            f"--grpc_python_out={output_dir}",
            str(proto_file),
        ],
        check=True,
    )

    # Fix imports in the generated grpc file
    grpc_file = output_dir / "search_pb2_grpc.py"
    fix_grpc_imports(grpc_file)


if __name__ == "__main__":
    generate_protos()
