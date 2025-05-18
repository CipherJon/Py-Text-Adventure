from setuptools import setup, find_packages

setup(
    name="text_adventure",
    version="0.1.0",  # Changed for semantic versioning
    author="Your Name",
    author_email="your.email@example.com",
    description="An interactive text-based adventure game",
    long_description=open('README.md', encoding='utf-8').read(),  # Added encoding
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/text_adventure",
    license="MIT",  # Explicitly added license
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",  # Added specific versions
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",  # Added for cross-platform
        "Intended Audience :: End Users/Desktop",  # Refined audience
        "Topic :: Games/Entertainment :: Role Playing",
    ],
    packages=find_packages(where="src", exclude=("tests", "docs")),  # Specified source and exclusions
    package_dir={"": "src"},  # Explicitly set package directory
    install_requires=[
        # Example: 'click>=8.0',  # Add dependencies if needed
    ],
    python_requires=">=3.8",  # Specified minimum Python version
    entry_points={
        "console_scripts": [
            "text-adventure=text_adventure.adventure:main",  # Hyphenated for CLI consistency
        ],
    },
    include_package_data=True,  # Added to include non-code files if needed
)