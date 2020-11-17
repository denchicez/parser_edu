
def get_social_links(links):
    prefixes = [['https://www.youtube.com/c/', 'https://www.youtube.com/channel/', 'https://www.youtube.com/user/'], ['https://vk.com/'], ['https://www.instagram.com/'], ['https://www.facebook.com/groups/', 'https://ru-ru.facebook.com/groups/'] ]
    socials = [''] * len(prefixes)
    for link in links:
        for i in range(len(prefixes)):
            val = ''
            for media in prefixes[i]:
                if (link.find(media) != -1):
                    val = link
            if (len(val) != 0):
                socials[i] = val
    result = {}
    if (len(socials[0]) != 0):
        result['youtube'] = socials[0]
    if (len(socials[1]) != 0):
        result['vk'] = socials[1]    
    if (len(socials[2]) != 0):
        result['inst'] = socials[2]   
    if (len(socials[3]) != 0):
        result['facebook'] = socials[3]       
    return result
my_links = {'https://www.instagram.com/_egor.bocharov/?hl=ru', 'https://vk.com/countryballs_re', 'https://ru-ru.facebook.com/groups/363858560447388/', 'https://www.youtube.com/c/Spoontamer'}
print(get_social_links(my_links))