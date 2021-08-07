import ldap3
from ldap3 import Server, Connection
from django.conf import settings

image_path = settings.MEDIA_ROOT


def connexion_ad2000(email_util, passw_util):
    server = Server('10.10.10.11', get_info=ldap3.ALL)
    try:
        # email_util = 'GROUPE-HASNAOUI\\' + email_util
        conn = Connection(server, email_util, passw_util, auto_bind=True)
        if (conn):
            ad_2000 = email_util.split('GROUPE-HASNAOUI\\')[1]
            conn.search(search_base="dc=groupe-hasnaoui,dc=local",
                        search_filter='(sAMAccountName=' + ad_2000 + ')',
                        attributes=('sAMAccountName', 'mail', 'title',
                                    'displayName', 'thumbnailPhoto'))

            Name = conn.entries[0].displayName.value
            mail = conn.entries[0].mail.value
            title = conn.entries[0].title.value
            ad_2000 = conn.entries[0].sAMAccountName.value
            thumbnailPhoto = conn.entries[0].thumbnailPhoto.value
            dict = {
                'name': Name,
                'mail': mail,
                'ad_2000': ad_2000,
                'title': title,
                "thumbnailPhoto": thumbnailPhoto
            }
            msg = dict
            print("yooooooo", f"{image_path}/{ad_2000}.png")
            open(f"{image_path}/{ad_2000}.png",
                 "wb").write(conn.entries[0].thumbnailPhoto.value)
        else:
            msg = 'deco'
    except Exception as e:
        msg = e
    return msg


def connexion_email(email_util, passw_util):
    server = Server('10.10.10.11', get_info=ldap3.ALL)
    try:
        conn = Connection(server, email_util, passw_util, auto_bind=True)
        if (conn):
            conn.search(search_base="dc=groupe-hasnaoui,dc=local",
                        search_filter='(mail=' + email_util + ')',
                        attributes=[
                            'sAMAccountName', 'mail', 'title', 'displayName',
                            'thumbnailPhoto'
                        ])
            Name = conn.entries[0].displayName.value
            mail = conn.entries[0].mail.value
            title = conn.entries[0].title.value
            ad_2000 = conn.entries[0].sAMAccountName.value
            thumbnailPhoto = conn.entries[0].thumbnailPhoto.value
            dict = {
                'name': Name,
                'mail': mail,
                'ad_2000': ad_2000,
                'title': title,
                'thumbnailPhoto': type(thumbnailPhoto)
            }
            msg = dict

            with open(f"{image_path}/{ad_2000}.png", "wb") as fh:
                fh.write(conn.entries[0].thumbnailPhoto.value)
        else:
            msg = 'deco'
    except Exception as e:
        msg = e

    return msg