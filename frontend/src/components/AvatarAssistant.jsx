import { useState } from "react";
import avatarImage from "../assets/leela-ai.png"
import { askPortfolioAssistant } from "../api/api";

function AvatarAssistant() {
    const [isOpen, setIsOpen] = useState(false);
    const [question, setQuestion] = useState("");
    const [messages, setMessages] = useState([]);
    const [sources, setSources] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState("");

    const handleSubmit = async (event) => {
        event.preventDefault();

        const trimmedQuestion = question.trim();

        if (!trimmedQuestion || isLoading) {
            return;
        }

        setMessages((currentMessages) => [
            ...currentMessages,
            {
                role: "user",
                content: trimmedQuestion,
            },
        ]);

        setQuestion("");
        setError("");
        setSources([]);
        setIsLoading(true);

        try {
            const response = await askPortfolioAssistant(trimmedQuestion);

            setMessages((currentMessages) => [
                ...currentMessages,
                {
                    role: "assistant",
                    content: response.answer,
                },
            ]);

            setSources(response.sources || []);
        } catch (requestError) {
            setError(
                requestError.message ||
                "The assistant could not answer the question.",            
            );
        } finally {
            setIsLoading(false);
        }
    };

    const handleSuggestion = (suggestion) => {
        setQuestion(suggestion);
    };


    return (
        <div className="assistant-wrapper">
            {!isOpen && (
                <div className="assistant-preview">
                    <div className="assistant-bubble">
                        Hi, I'm Leela AI 👋 
                        <br />
                        Ask me about Leela
                    </div>

                    <button
                        className="assistant-avatar"
                        onClick={() => setIsOpen(true)}
                        aria-label="Open Leela AI assistant"
                    >
                        <img
                            src={avatarImage}
                            alt="Leela AI assistant"
                            className="assistant-avatar-image"
                            />
                            
                        <span className="online-dot"></span> 
                    </button>
                </div>
            )}

            {isOpen && (
                <div className="assistant-chat glass">
                    <div className="assistant-chat-header">
                        <div className="assistant-header-profile">
                            <img
                                src={avatarImage}
                                alt=""
                                className="assistant-header-avatar"
                            />
                            <div>
                                <h3>Leela AI</h3>
                                <p>
                                    <span className="small-online-dot"></span>
                                    Online
                                </p>
                            </div>
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

                        {messages.length === 0 && (
                            <div className="assistant-suggestions">
                                <button
                                    type="button"
                                    onClick={() =>
                                        handleSuggestion(
                                        "What projects has Leela built?",
                                        )
                                    }
                                >
                                    What projects has Leela built?
                                </button>

                                <button
                                    type="button"
                                    onClick={() =>
                                        handleSuggestion(
                                            "What technologies does Leela use?",
                                        )
                                    }
                                >
                                    What technologies does Leela use?
                                </button>

                                <button
                                    type="button"
                                    onClick={() =>
                                        handleSuggestion(
                                        "Tell me about Leela's dissertation.",
                                        )
                                    }
                                >
                                    Tell me about her dissertation
                                </button>
                            </div>
                        )}

                        <div className="assistant-conversation">
                            {messages.map((message, index) => (
                                <div className={'chat-message ${message.role}'}
                                key={'${message.role}-${index}'}
                                >
                                    {message.content}
                                </div>
                            ))}

                            {isLoading && (
                                <div className="chat-message assistant loading-message">
                                    Leela AI is thinking...
                                </div>
                            )}

                            {error && (
                                <div className="assistant-error">
                                    {error}
                                </div>
                            )}

                            {sources.length > 0 && (
                                <div className="assistant-sources">
                                    <p>Sources</p>

                                    {sources.map((source, index) => (
                                        <div
                                        className="source-card"
                                        key={source.chunk_id || source.source || index}
                                        >
                                            <strong>{source.title || `Source ${index + 1 }`}</strong>
                                            <span>{source.section || source.document_type}</span>
                                        </div>
                                    ))}
                                </div>
                            )}
                        </div>
                    </div>

                    <form
                        className="assistant-input"
                        onSubmit={handleSubmit}
                    >
                        <input
                            type="text"
                            value={question}
                            onChange={(event) =>
                                setQuestion(event.target.value)
                            }
                            placeholder="Ask about Leela..."
                            disabled={isLoading}
                            aria-label="Question for Leela AI"
                        />

                        <button
                            type="submit"
                            disabled={isLoading || !question.trim()}
                            aria-label="Send question"
                        >
                            ➜
                        </button>
                    </form>
                </div>
            )}
        </div>
    );
}

export default AvatarAssistant;