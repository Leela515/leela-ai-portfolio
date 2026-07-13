function Hero() {
    return (
        <section className="hero">
            <div className="hero-content">
                <p className="eyebrow">AI Portfolio</p>
                <h1>
                    Leela <span>R</span>
                </h1>

                <h2>AI Engineer
                    <span className="gradient-text"></span>
                </h2>
                <div className="hero-tags">
                    <span>NLP</span>
                    <span>Computer Vision</span>
                    <span>Generative AI</span>
                    <span>RAG</span>
                </div>

                <p className="hero-description">
                Building intelligent AI systems that combine research, deep learning, and production-ready engineering.
                </p>

                <div className="hero-buttons">
                    <button className="primary-button">View Projects</button>
                    <button className="secondary-button">Download Resume</button>
                </div>
            </div>
        </section>
    );

}

export default Hero;