import phind

# set cf_clearance cookie (needed again)
phind.cf_clearance = "w2rpdQJw7nd1cKNY_Fno_vbWwXVQGeKekZelSHGuKnk-1682533636-0-160"
phind.user_agent ="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0"
prompt = 'What is the sentiment of the following: i feel so horrible'

# normal completion
result = phind.Completion.create(
    model  = 'gpt-4',
    prompt = prompt,
    results     = phind.Search.create(prompt, actualSearch = False), # create search (set actualSearch to False to disable internet)
    creative    = False,
    detailed    = False,
    codeContext = '') # up to 3000 chars of code

print(result.completion.choices[0].text)