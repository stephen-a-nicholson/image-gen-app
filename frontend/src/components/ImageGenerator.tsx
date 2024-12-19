import React, { useState } from 'react';

interface GenerateImageResponse {
  success: boolean;
  image: string;
  prompt: string;
}

const ImageGenerator: React.FC = () => {
  const [prompt, setPrompt] = useState<string>('');
  const [image, setImage] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const generateImage = async (): Promise<void> => {
    try {
      setLoading(true);
      setError(null);
      
      const response = await fetch('http://localhost:8000/image/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        },
        body: JSON.stringify({ prompt })
      });

      if (!response.ok) {
        throw new Error('Failed to generate image');
      }

      const data: GenerateImageResponse = await response.json();
      setImage(data.image);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto mt-8 p-6 bg-white rounded-lg shadow-lg">
      <div className="mb-6">
        <h2 className="text-2xl font-bold mb-4">AI Image Generator</h2>
      </div>
      <div className="space-y-4">
        <div className="flex gap-2">
          <input
            type="text"
            value={prompt}
            onChange={(e: React.ChangeEvent<HTMLInputElement>) => setPrompt(e.target.value)}
            placeholder="Enter your image prompt..."
            disabled={loading}
            className="flex-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button 
            onClick={generateImage} 
            disabled={!prompt || loading}
            className="px-4 py-2 bg-blue-500 text-white rounded-lg disabled:opacity-50 hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            {loading ? (
              <span className="flex items-center">
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Generating
              </span>
            ) : (
              'Generate'
            )}
          </button>
        </div>

        {error && (
          <div className="text-red-500 text-sm">{error}</div>
        )}

        {image && (
          <div className="mt-4">
            <img 
              src={image} 
              alt="Generated" 
              className="w-full rounded-lg shadow-lg"
            />
            <p className="text-sm text-gray-500 mt-2">
              Generated using Stable Diffusion XL by Stability AI
            </p>
          </div>
        )}
      </div>
    </div>
  );
};

export default ImageGenerator;