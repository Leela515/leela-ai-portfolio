import { useState } from "react";

function AvatarAssistant() {
    const [isOpen, setIsOpen] = useState(false);
    return (
        <div className="assistant-wrapper">
        {!isOpen && (
            <div className="assistant-preview">
                <div className="assistant-bubble">
                    Hi 👋 <br />
                    Ask Leela AI
                </div>

                <button
                    className="assistant-avatar"
                    onClick={() => setIsOpen(true)}
                    aria-label="Open Leela AI assistant"
                >
                    👩🏻‍💻
                    <span className="online-dot"></span> 
                </button>
            </div>
        )}

        {isOpen && (
            <div className="assistant-chat glass">
                <div className="assistant-chat-header">
                    <div>
                        <h3>Leela AI</h3>
                        <p>
                            <span className="small-online-dot"></span>
                            Online
                        </p>
                    </div>

                    <button
                        className="assistant-close"
                        onClick={() => setIsOpen(false)}
                        aria-label="Close assistant"
                    >
                       × 
                    </button>
                </div>

                <div className="assistant-chat-body">
                    <div className="assistant-message">
                        Hi, I'm Leela AI 👋 
                        <br />
                        Ask me about Leela's projects, skills, research, or experience.
                    </div>

                    <div className="assistant-suggestions">
                        <button>What projects has Leela built?</button>
                        <button>What technologies does she use?</button>
                        <button>Tell me about her dissertation</button>
                    </div>
                </div>

                <div className="assistant-input">
                    <input placeholder="Ask about Leela..." />
                    <button>➜</button>
                </div>
            </div>
        )}
         
        </div>
    );
}

export default AvatarAssistant;