// OpenAIAPI implementation with model "gpt-4o" using a personal GITHUB_TOKEN
class OpenAIAPI {
    static async generateResponse(userMessage, conversationHistory = []) {
        const apiKey = process.env.GITHUB_TOKEN;
        const endpoint = 'https://models.inference.ai.azure.com';
        const modelName = "gpt-4o";
        const OpenAI = require('openai');

        const client = new OpenAI({ baseURL: endpoint, apiKey: apiKey });

        const response = await client.chat.completions.create({
            messages: conversationHistory.concat([{ role: 'user', content: userMessage }]),
            temperature: 1.0,
            top_p: 1.0,
            max_tokens: 150,
            model: modelName
          });
      
        const responseData = await response;
        // Log the entire API response for debugging
        console.log('Response from OpenAI API:', responseData.choices[0].message);
        // Check if choices array is defined and not empty
        if (responseData.choices && responseData.choices.length > 0 && responseData.choices[0].message) {
            return responseData.choices[0].message.content;
        } else {
            // Handle the case where choices array is undefined or empty
            console.error('Error: No valid response from OpenAI API');
            return 'Sorry, I couldn\'t understand that.';
        }
    }
}

module.exports = { OpenAIAPI };