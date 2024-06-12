import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    connected_pages = corpus[page]
    # if there is no pages that the page has links to
    # return probability distribution with the same probability for all the pages
    if not connected_pages:
        return {p: 1 / len(corpus) for p in corpus}

    # else calculate the probabilities
    base_value = (1-damping_factor) / len(corpus)
    res = {p: base_value for p in corpus if p not in connected_pages}

    for p in connected_pages:
        to_add = damping_factor / len(connected_pages)
        res[p] = base_value + to_add

    return res


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page = random.choice(list(corpus.keys()))

    res = {i: 0 for i in corpus}
    for _ in range(n):
        # get a transition model basing on the page
        t_model = transition_model(corpus=corpus, page=page, damping_factor=damping_factor)

        # get the new page basing on the probability distribution from the transition model
        keys = list(t_model.keys())
        vals = list(t_model.values())
        page = random.choices(keys, weights=vals, k=1)[0]

        # add the results to the main dict
        for k, v in t_model.items():
            res[k] += v

    # prepare the final data to sum to be equal 1
    total = sum(i for i in res.values())
    return {key: value / total for key, value in res.items()}


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    def pages_that_link_to_page(page: str, corpus: dict[str, set[str]]) -> set[str]:
        return {key for key, vals in corpus.items() if page in vals}

    pages_amount = len(corpus)
    res = {k: 1 / pages_amount for k in corpus}

    not_changing = set()
    while len(not_changing) < pages_amount:
        for k, v in res.items():
            pages_that_link = pages_that_link_to_page(page=k, corpus=corpus)

            len_pages = len(pages_that_link)
            if not len_pages:
                len_pages = pages_amount

            # calculate the PageRank
            first_part = (1 - damping_factor) / pages_amount
            second_part = damping_factor * sum(res[p] / (len(corpus[p]) if corpus[p] else pages_amount) for p in pages_that_link)

            new_val = first_part + second_part
            res[k] = new_val

            # track if the PR not changing
            if abs(v - new_val) <= 0.001:
                not_changing.add(k)
            else:
                if k in not_changing:
                    not_changing.remove(k)

    return res


if __name__ == "__main__":
    main()
