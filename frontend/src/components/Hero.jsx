function Hero() {
    return (
        <section className="hero">
            <div className="hero-content">
                <p className="eyebrow">AI Portfolio</p>
                <h1>Leela R</h1>

                <h2>AI Engineer • NLP • Computer Vision • Generative AI</h2>

                <p className="hero-description">
                Building intelligent AI systems that combine research, deep learning, and production-ready engineering.
                </p>

                <div className="hero-button">
                    <button className="primary-button">View Projects</button>
                    <button className="secondary-button">Download Resume</button>
                </div>
            </div>

            <div className="hero-visual">
                <div className="glow-card">
                    <p className="card-label">Leela AI</p>
                    <h3>Ask my portfolio anything.</h3>
                    <span>
                        Recruiters can ask about my projects, skills, research, experience, and technical decisions.
                    </span>
                </div>
            </div>
        </section>
    );

}

export default Hero;