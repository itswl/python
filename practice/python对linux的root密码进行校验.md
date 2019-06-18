**因为最近因为安全问题，将密码不再写到配置文件中**

为了防止自己手残，输入错误的密码，导致后续某一步运行失败，于是在运行前，就对密码进行校验。

```
import crypt

p = os.popen('cat /etc/shadow|grep root')
shadow_rootline = p.read()
_password = shadow_rootline.split(':')[1]

password = ''
salt = re.findall('\$[\s\S]*?\$[\s\S]*?\$',_password)[0]
crypt_password = crypt.crypt(password,salt)



while crypt_password != _password:
    print('\n[ warning ] root password may be incorrect \n')
    password = getpass.getpass('please input root password:')
    crypt_password = crypt.crypt(password,salt)

```
