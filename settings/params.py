# *_*coding:utf-8 *_*
"""
Descri：
"""


class wordcloud:
    r"""Word cloud object for generating and drawing.

    Parameters
    ----------
    font_path : string
        Font path to the font that will be used (OTF or TTF).
        Defaults to DroidSansMono path on a Linux machine. If you are on
        another OS or don't have this font, you need to adjust this path.

    width : int (default=400)
        Width of the canvas.

    height : int (default=200)
        Height of the canvas.

    prefer_horizontal : float (default=0.90)
        The ratio of times to try horizontal fitting as opposed to vertical.
        If prefer_horizontal < 1, the algorithm will try rotating the word
        if it doesn't fit. (There is currently no built-in way to get only
        vertical words.)

    mask : nd-array or None (default=None)
        If not None, gives a binary mask on where to draw words. If mask is not
        None, width and height will be ignored and the shape of mask will be
        used instead. All white (#FF or #FFFFFF) entries will be considerd
        "masked out" while other entries will be free to draw on. [This
        changed in the most recent version!]

    contour_width: float (default=0)
        If mask is not None and contour_width > 0, draw the mask contour.

    contour_color: color value (default="black")
        Mask contour color.

    scale : float (default=1)
        Scaling between computation and drawing. For large word-cloud images,
        using scale instead of larger canvas size is significantly faster, but
        might lead to a coarser fit for the words.

    min_font_size : int (default=4)
        Smallest font size to use. Will stop when there is no more room in this
        size.

    font_step : int (default=1)
        Step size for the font. font_step > 1 might speed up computation but
        give a worse fit.

    max_words : number (default=200)
        The maximum number of words.

    stopwords : set of strings or None
        The words that will be eliminated. If None, the build-in STOPWORDS
        list will be used. Ignored if using generate_from_frequencies.

    background_color : color value (default="black")
        Background color for the word cloud image.

    max_font_size : int or None (default=None)
        Maximum font size for the largest word. If None, height of the image is
        used.

    mode : string (default="RGB")
        Transparent background will be generated when mode is "RGBA" and
        background_color is None.

    relative_scaling : float (default='auto')
        Importance of relative word frequencies for font-size.  With
        relative_scaling=0, only word-ranks are considered.  With
        relative_scaling=1, a word that is twice as frequent will have twice
        the size.  If you want to consider the word frequencies and not only
        their rank, relative_scaling around .5 often looks good.
        If 'auto' it will be set to 0.5 unless repeat is true, in which
        case it will be set to 0.

        .. versionchanged: 2.0
            Default is now 'auto'.

    color_func : callable, default=None
        Callable with parameters word, font_size, position, orientation,
        font_path, random_state that returns a PIL color for each word.
        Overwrites "colormap".
        See colormap for specifying a matplotlib colormap instead.
        To create a word cloud with a single color, use
        ``color_func=lambda *args, **kwargs: "white"``.
        The single color can also be specified using RGB code. For example
        ``color_func=lambda *args, **kwargs: (255,0,0)`` sets color to red.

    regexp : string or None (optional)
        Regular expression to split the input text into tokens in process_text.
        If None is specified, ``r"\w[\w']+"`` is used. Ignored if using
        generate_from_frequencies.

    collocations : bool, default=True
        Whether to include collocations (bigrams) of two words. Ignored if using
        generate_from_frequencies.


        .. versionadded: 2.0

    colormap : string or matplotlib colormap, default="viridis"
        Matplotlib colormap to randomly draw colors from for each word.
        Ignored if "color_func" is specified.

        .. versionadded: 2.0

    normalize_plurals : bool, default=True
        Whether to remove trailing 's' from words. If True and a word
        appears with and without a trailing 's', the one with trailing 's'
        is removed and its counts are added to the version without
        trailing 's' -- unless the word ends with 'ss'. Ignored if using
        generate_from_frequencies.

    repeat : bool, default=False
        Whether to repeat words and phrases until max_words or min_font_size
        is reached.

    include_numbers : bool, default=False
        Whether to include numbers as phrases or not.

    min_word_length : int, default=0
        Minimum number of letters a word must have to be included.

    collocation_threshold: int, default=30
        Bigrams must have a Dunning likelihood collocation score greater than this
        parameter to be counted as bigrams. Default of 30 is arbitrary.

        See Manning, C.D., Manning, C.D. and Schütze, H., 1999. Foundations of
        Statistical Natural Language Processing. MIT press, p. 162
        https://nlp.stanford.edu/fsnlp/promo/colloc.pdf#page=22

    Attributes
    ----------
    ``words_`` : dict of string to float
        Word tokens with associated frequency.

        .. versionchanged: 2.0
            ``words_`` is now a dictionary

    ``layout_`` : list of tuples (string, int, (int, int), int, color))
        Encodes the fitted word cloud. Encodes for each word the string, font
        size, position, orientation and color.

    Notes
    -----
    Larger canvases with make the code significantly slower. If you need a
    large word cloud, try a lower canvas size, and set the scale parameter.

    The algorithm might give more weight to the ranking of the words
    than their actual frequencies, depending on the ``max_font_size`` and the
    scaling heuristic.
    """
    WIDTH = 800
    HEIGHT = 600
    MARGIN = 2
    RANKS_ONLY = True
    MAX_WORDS = 200
    COLLECTIONS = False


class word2vec:
    r"""Word2vec Parameters

    Parameters
    ----------
    sentences : iterable of iterables, optional
        The `sentences` iterable can be simply a list of lists of tokens, but for larger corpora,
        consider an iterable that streams the sentences directly from disk/network.
        See :class:`~gensim.models.word2vec.BrownCorpus`, :class:`~gensim.models.word2vec.Text8Corpus`
        or :class:`~gensim.models.word2vec.LineSentence` in :mod:`~gensim.models.word2vec` module for such examples.
        See also the `tutorial on data streaming in Python
        <https://rare-technologies.com/data-streaming-in-python-generators-iterators-iterables/>`_.
        If you don't supply `sentences`, the model is left uninitialized -- use if you plan to initialize it
        in some other way.
    corpus_file : str, optional
        Path to a corpus file in :class:`~gensim.models.word2vec.LineSentence` format.
        You may use this argument instead of `sentences` to get performance boost. Only one of `sentences` or
        `corpus_file` arguments need to be passed (or none of them, in that case, the model is left uninitialized).
    size : int, optional
        Dimensionality of the word vectors.
    window : int, optional
        Maximum distance between the current and predicted word within a sentence.
    min_count : int, optional
        Ignores all words with total frequency lower than this.
    workers : int, optional
        Use these many worker threads to train the model (=faster training with multicore machines).
    sg : {0, 1}, optional
        Training algorithm: 1 for skip-gram; otherwise CBOW.
    hs : {0, 1}, optional
        If 1, hierarchical softmax will be used for model training.
        If 0, and `negative` is non-zero, negative sampling will be used.
    negative : int, optional
        If > 0, negative sampling will be used, the int for negative specifies how many "noise words"
        should be drawn (usually between 5-20).
        If set to 0, no negative sampling is used.
    ns_exponent : float, optional
        The exponent used to shape the negative sampling distribution. A value of 1.0 samples exactly in proportion
        to the frequencies, 0.0 samples all words equally, while a negative value samples low-frequency words more
        than high-frequency words. The popular default value of 0.75 was chosen by the original Word2Vec paper.
        More recently, in https://arxiv.org/abs/1804.04212, Caselles-Dupré, Lesaint, & Royo-Letelier suggest that
        other values may perform better for recommendation applications.
    cbow_mean : {0, 1}, optional
        If 0, use the sum of the context word vectors. If 1, use the mean, only applies when cbow is used.
    alpha : float, optional
        The initial learning rate.
    min_alpha : float, optional
        Learning rate will linearly drop to `min_alpha` as training progresses.
    seed : int, optional
        Seed for the random number generator. Initial vectors for each word are seeded with a hash of
        the concatenation of word + `str(seed)`. Note that for a fully deterministically-reproducible run,
        you must also limit the model to a single worker thread (`workers=1`), to eliminate ordering jitter
        from OS thread scheduling. (In Python 3, reproducibility between interpreter launches also requires
        use of the `PYTHONHASHSEED` environment variable to control hash randomization).
    max_vocab_size : int, optional
        Limits the RAM during vocabulary building; if there are more unique
        words than this, then prune the infrequent ones. Every 10 million word types need about 1GB of RAM.
        Set to `None` for no limit.
    max_final_vocab : int, optional
        Limits the vocab to a target vocab size by automatically picking a matching min_count. If the specified
        min_count is more than the calculated min_count, the specified min_count will be used.
        Set to `None` if not required.
    sample : float, optional
        The threshold for configuring which higher-frequency words are randomly downsampled,
        useful range is (0, 1e-5).
    hashfxn : function, optional
        Hash function to use to randomly initialize weights, for increased training reproducibility.
    iter : int, optional
        Number of iterations (epochs) over the corpus.
    trim_rule : function, optional
        Vocabulary trimming rule, specifies whether certain words should remain in the vocabulary,
        be trimmed away, or handled using the default (discard if word count < min_count).
        Can be None (min_count will be used, look to :func:`~gensim.utils.keep_vocab_item`),
        or a callable that accepts parameters (word, count, min_count) and returns either
        :attr:`gensim.utils.RULE_DISCARD`, :attr:`gensim.utils.RULE_KEEP` or :attr:`gensim.utils.RULE_DEFAULT`.
        The rule, if given, is only used to prune vocabulary during build_vocab() and is not stored as part of the
        model.

        The input parameters are of the following types:
            * `word` (str) - the word we are examining
            * `count` (int) - the word's frequency count in the corpus
            * `min_count` (int) - the minimum count threshold.
    sorted_vocab : {0, 1}, optional
        If 1, sort the vocabulary by descending frequency before assigning word indexes.
        See :meth:`~gensim.models.word2vec.Word2VecVocab.sort_vocab()`.
    batch_words : int, optional
        Target size (in words) for batches of examples passed to worker threads (and
        thus cython routines).(Larger batches will be passed if individual
        texts are longer than 10000 words, but the standard cython code truncates to that maximum.)
    compute_loss: bool, optional
        If True, computes and stores loss value which can be retrieved using
        :meth:`~gensim.models.word2vec.Word2Vec.get_latest_training_loss`.
    callbacks : iterable of :class:`~gensim.models.callbacks.CallbackAny2Vec`, optional
        Sequence of callbacks to be executed at specific stages during training.

    Examples
    --------
    Initialize and train a :class:`~gensim.models.word2vec.Word2Vec` model

    .. sourcecode:: pycon

        >>> from gensim.models import Word2Vec
        >>> sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]
        >>> model = Word2Vec(sentences, min_count=1)

    """
    HS = 1
    MIN_COUNT = 1
    WINDOW = 3
    SIZE = 100


if __name__ == "__main__":
    print(word2vec.SIZE)
