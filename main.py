import file_extraction as fe

if __name__ == "__main__":
    print("Hello, World!")
    fe.unzip_dataset('./data_sentiment_analysis.zip', './extracted_dataset')
