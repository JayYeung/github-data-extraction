## List of Things Fixed (should prolly mention during meeting)

1. Fixed code pushing in random stuff into CSV
    - 1a. Code would push rate limit errors, repo not found errors (as README)
    - 1b. Code would use append instead of dictionaries for some reason
2. Push data every 10 repositories to avoid losing data in between runs
3. Fixed code sometimes getting the wrong README URL
4. Fixed code creating duplicate files in topics and data
5. Created soft fix for rate limit error. Old solution will just return an errored content
6. Used concurrency to run more requests at once
7. Cleaned up most of the code
8. Run with 6 accounts instead of 1

## TODO

1. README can be named differently, i.e., `readme.md`, `README.rst`, `readme.txt`, etc.
2. Set sleep time to exact reset time
3. automatically label the data with default number
