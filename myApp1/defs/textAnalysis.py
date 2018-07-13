import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
""" before nltk, do:
pip install nltk
on mac:
    # https://stackoverflow.com/questions/41348621/ssl-error-downloading-nltk-data
    cd /Applications/Python 3.6/
    ./Install Certificates.command
on Linux
    sh "/Applications/Python\ 3.6/Install\ Certificates.command"
nltk.download('stopwords')
nltk.download('punkt')
"""

PRE_TAGS = ['programming', 'python', 'r', 'scala', 'javascript', 'web',
'dashboard', 'data', 'bigdata', 'hdfs', 'spark', 'kudu', 'datascience',
'machine', 'learning', 'ai', 'ml', 'artificial', 'intelligence', 'deep',
'visualization', 'd3', 'd3js', 'dcjs',
'frontend', 'backend', 'vue', 'vuejs',
'learn', 'do', 'todo', 'practice', 'revise'
]

#region urlHtmlChar
def urlExtract(note):
    # note="""
    # Learn "Stopwords" for search engines: this is a list of words that search engines would remove from the search terms to optimize their searches!
    # https://www.ranks.nl/stopwords and then do this with http://asgh.co.in
    # 1. this is a bullet point
    # * this is more bullet points!
    # need to learn this more
    # I need to learn and practice this
    # this is digit and char se7en movie like!
    # <this> is some <h2> html </h2> text</this>
    # """
    regPat = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    return([re.sub(regPat, '', note)] + re.findall(regPat, note))

def htmlExtract(note):
    # below regex needs to be modified
    regPat = r'<[^>]+>'
    return re.sub(regPat, '', note)

def removeQuotedWords(note):
    # use this for business logic if words from quotes should not be considered for tags!
    regPat = '\".+\"\s?'
    return re.sub(regPat, '', note)

#endregion

#region nltkProcessing
def remStopWords(note):
    noteNoUrl = urlExtract(note)[0]
    noteNoHtml = htmlExtract(noteNoUrl)
    noteNoSpChar = re.sub(r'[\W]', ' ', noteNoHtml)
    noteNoDigit = re.sub(r'[\d]', ' ', noteNoSpChar)
    noteCleaned = noteNoDigit
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(noteCleaned)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    return filtered_sentence

def convLower(noteAr):
    return [w.lower() for w in noteAr]

def getFreq(noteAr):
    """
    this generates a note array dictionary which is sorted
    by frequency of word occurrence!
    
    """

    BAD_CHARS = ".!?,\'\""
    words = [ word.strip(BAD_CHARS) for word in noteAr ]
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    tx = [ (v, k) for (k, v) in word_freq.items()]
    tx.sort(reverse=True)
    word_freq_sorted = [ (k, v) for (v, k) in tx ]
    return word_freq_sorted

#endregion

#region getTags

def getPreTags(noteAr, PRE_TAGS):
    """
    """
    return list(set([w for w in noteAr if w in PRE_TAGS]))

def removePreTags(noteAr):
    return [w for w in noteAr if w not in getPreTags(noteAr)]


#endregion