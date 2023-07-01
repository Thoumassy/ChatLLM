from langchain.document_loaders import DirectoryLoader

loader = DirectoryLoader(
    'Data/', # my local directory
    glob='**/*.pdf',     # we only get pdfs
    show_progress=True
)
docs = loader.load()
docs

