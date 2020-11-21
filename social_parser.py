def get_social_links(links):
    prefixes = [['https://www.youtube.com/c/', 'https://www.youtube.com/channel/', 'https://www.youtube.com/user/'], ['https://vk.com/'], ['https://www.instagram.com/'], ['https://www.facebook.com/groups/', 'https://ru-ru.facebook.com/groups/'] ]
    socials = [[]] * len(prefixes)
    for link in links:
        for i in range(len(prefixes)):
            val = ''
            for media in prefixes[i]:
                if (link.find(media) != -1):
                    val = link
            if (len(val) != 0):
                socials[i].append(val)
    result = {}
    if (len(socials[0]) != 0):
        resLink = socials[0][0]
        val = -1
        for link in socials[0]:
            follow = 0 # заменить за GetYouTube
            if (follow > val):
                val = follow
                resLink = link
        result['youtube'] = resLink
    if (len(socials[1]) != 0):
        resLink = socials[0][0]
        val = -1
        for link in socials[0]:
            follow = 0 # заменить за GetVk
            if (follow > val):
                val = follow
                resLink = link
        result['vk'] = resLink   
    if (len(socials[2]) != 0):
        resLink = socials[0][0]
        val = -1
        for link in socials[0]:
            follow = 0 # заменить за GetInst
            if (follow > val):
                val = follow
                resLink = link
        result['inst'] = resLink  
    if (len(socials[3]) != 0):
        result['facebook'] = socials[3][0] # так как facebook не получается, берем единственную ссылку       
    return result
my_links = {'https://www.instagram.com/_egor.bocharov/?hl=ru', 'https://vk.com/countryballs_re', 'https://ru-ru.facebook.com/groups/363858560447388/', 'https://www.youtube.com/c/Spoontamer'}
print(get_social_links(my_links))
