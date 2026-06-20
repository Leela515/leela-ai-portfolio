from backend.app.rag.models import DocumentChunk
from backend.app.rag.text_builder import RetrievalTextBuilder


def test_retrieval_text_builder_includes_section_and_content():
    chunk = DocumentChunk(
        source="underwater_pose_estimation.md",
        section="Technology Stack",
        content="PyTorch, OpenCV, RTMDet, RTMPose",
        chunk_id="chunk-1",
    )

    builder = RetrievalTextBuilder()
    text = builder.build_text(chunk)

    assert "Technology Stack" in text
    assert "PyTorch" in text
    assert "Content:" in text
    assert "underwater_pose_estimation.md" not in text