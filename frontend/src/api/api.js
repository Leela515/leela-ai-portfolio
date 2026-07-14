const API_BASE_URL = 
    import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export async function askPortfolioAssistant(question) {
    const response = await fetch(`${API_BASE_URL}/chat`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            question,
        }),
    });

    if (!response.ok) {
        let message = "The portfolio assistant is currently unavailable.";

        try {
            const errorData = await response.json();

            if (errorData.detail) {
                message = errorData.detail;
            }
        } catch {
            // Keep the fallback message when the response is not JSON.
        }

        throw new Error(message);
    }

    return response.json();
}