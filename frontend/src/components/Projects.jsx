function Projects() {
    return (
        <section id="projects"className="section">
            <h2>Projects</h2>

            <h3>Natural Language Processing</h3>

            <div className="project-card">
                <h4>Spiking Transformer Language Model</h4>

                <p>
                    Developed a fully spiking Transformer architecture for energy-efficient language modelling.
                </p>
            </div>

            <div className="project-card">
                <h4>AI Research Assistant</h4>

                <p>
                    Production-style RAG assistant using FastAPI, FAISS, Cross-encoder reranking, and Ollama.
                </p>
            </div>

            <h3>Computer Vision</h3>
            <div className="project-card">
                <h4>Underwater Swimmer Pose Estimation</h4>

                <p>
                    Built a two-stage RTMDet + RTMPose pipeline for underwater swimmer analysis.
                </p>
            </div>
        </section>
    );
}

export default Projects;