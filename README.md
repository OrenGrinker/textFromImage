# TextFromImage

![Python Version](https://img.shields.io/pypi/pyversions/textfromimage)
![PyPI Version](https://img.shields.io/pypi/v/textfromimage)
![License](https://img.shields.io/pypi/l/textfromimage)
![Downloads](https://img.shields.io/pypi/dm/textfromimage)

A powerful Python library for obtaining detailed descriptions of images using various AI models including OpenAI's GPT models, Azure OpenAI, and Anthropic Claude. Perfect for applications requiring image understanding, accessibility features, and content analysis. Supports both local files and URLs, with batch processing capabilities.

## 🌟 Key Features

- 🤖 **Multiple AI Providers**: Support for OpenAI, Azure OpenAI, and Anthropic Claude
- 🌐 **Flexible Input**: Support for both URLs and local file paths
- 📦 **Batch Processing**: Process multiple images (up to 20) concurrently
- 🔄 **Flexible Integration**: Easy-to-use API with multiple initialization options
- 🎯 **Custom Prompting**: Configurable prompts for targeted descriptions
- 🔑 **Secure Authentication**: Multiple authentication methods including environment variables
- 🛠️ **Model Selection**: Support for different model versions and configurations
- 📝 **Type Hints**: Full typing support for better development experience

## 📦 Installation

```bash
pip install textfromimage

# With Azure support
pip install textfromimage[azure]

# With all optional dependencies
pip install textfromimage[all]
```

## 🚀 Quick Start

```python
import textfromimage

# Initialize with API key
textfromimage.openai.init(api_key="your-openai-api-key")

# Process single image (URL or local file)
image_url = 'https://example.com/image.jpg'
local_image = '/path/to/local/image.jpg'

# Get description from URL
url_description = textfromimage.openai.get_description(image_path=image_url)

# Get description from local file
local_description = textfromimage.openai.get_description(image_path=local_image)

# Batch processing
image_paths = [
    'https://example.com/image1.jpg',
    '/path/to/local/image2.jpg',
    'https://example.com/image3.jpg'
]

batch_results = textfromimage.openai.get_description_batch(
    image_paths=image_paths,
    concurrent_limit=3  # Process 3 images at a time
)

# Process results
for result in batch_results:
    if result.success:
        print(f"Success for {result.image_path}: {result.description}")
    else:
        print(f"Failed for {result.image_path}: {result.error}")
```

## 💡 Advanced Usage

### 🤖 Multiple Provider Support

```python
# Anthropic Claude Integration
textfromimage.claude.init(api_key="your-anthropic-api-key")

# Single image
claude_description = textfromimage.claude.get_description(
    image_path=image_path,
    model="claude-3-sonnet-20240229"
)

# Batch processing
claude_results = textfromimage.claude.get_description_batch(
    image_paths=image_paths,
    model="claude-3-sonnet-20240229",
    concurrent_limit=3
)

# Azure OpenAI Integration
textfromimage.azure_openai.init(
    api_key="your-azure-openai-api-key",
    api_base="https://your-azure-endpoint.openai.azure.com/",
    deployment_name="your-deployment-name"
)

# Single image with system prompt
azure_description = textfromimage.azure_openai.get_description(
    image_path=image_path,
    system_prompt="Analyze this image in detail"
)

# Batch processing
azure_results = textfromimage.azure_openai.get_description_batch(
    image_paths=image_paths,
    system_prompt="Analyze each image in detail",
    concurrent_limit=3
)
```

### 🔧 Configuration Options

```python
# Environment Variable Configuration
import os
os.environ['OPENAI_API_KEY'] = 'your-openai-api-key'
os.environ['ANTHROPIC_API_KEY'] = 'your-anthropic-api-key'
os.environ['AZURE_OPENAI_API_KEY'] = 'your-azure-openai-api-key'
os.environ['AZURE_OPENAI_ENDPOINT'] = 'your-azure-endpoint'
os.environ['AZURE_OPENAI_DEPLOYMENT'] = 'your-deployment-name'

# Custom options for batch processing
batch_results = textfromimage.openai.get_description_batch(
    image_paths=image_paths,
    model='gpt-4-vision-preview',
    prompt="Describe the main elements of each image",
    max_tokens=300,
    concurrent_limit=5
)
```

## 📋 Parameters and Types

```python
# Single image processing parameters
def get_description(
    image_path: str,
    prompt: str = "What's in this image?",
    max_tokens: int = 300,
    model: str = "gpt-4-vision-preview"
) -> str: ...

# Batch processing result type
@dataclass
class BatchResult:
    success: bool
    description: Optional[str]
    error: Optional[str]
    image_path: str

# Batch processing parameters
def get_description_batch(
    image_paths: List[str],
    prompt: str = "What's in this image?",
    max_tokens: int = 300,
    model: str = "gpt-4-vision-preview",
    concurrent_limit: int = 3
) -> List[BatchResult]: ...
```

## 🔍 Error Handling

```python
from textfromimage.utils import BatchResult

# Single image processing
try:
    description = textfromimage.openai.get_description(image_path=image_path)
except ValueError as e:
    print(f"Image processing error: {e}")
except RuntimeError as e:
    print(f"API error: {e}")

# Batch processing error handling
results = textfromimage.openai.get_description_batch(image_paths)
successful = [r for r in results if r.success]
failed = [r for r in results if not r.success]

for result in failed:
    print(f"Failed to process {result.image_path}: {result.error}")
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.