
from boilerpy3 import extractors
from gensim.summarization.summarizer import summarize

#Sample
#Long article
sample = 'https://healthinformatics.uic.edu/blog/the-impact-of-health-informatics-on-nursing-practice/'

def tldr(link= sample):
    '''
    Produces a coherent summary in 4-5 sentences from a given url.
    Inputs:
        link: (string) the url of the webpage
    Returns: a list of string
    '''
    #I use word_count as 150 to limit the summary to 4-5 sentences
    wc =150

    extractor = extractors.ArticleExtractor()
    # From a URL
    content = extractor.get_content_from_url(str(link))
    
    
    rv = summarize(content, split=True)
    while len(rv) >5:
      rv = summarize(content, word_count=wc, split=True)
      wc -= 10
      
    print("The original link is: " + link )
    print("The summary is:")
    return rv
