from setuptools import setup, find_packages

setup(
    name="image_text_localization",
    version="0.1.0", 
    description="Extract text from images and determine image location using NLP and OCR",
    author="201835457 박재민",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "opencv-python",
        "pytesseract",
        "transformers",
        "Pillow",
        "exifread",
    ],  # 의존성 패키지
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
