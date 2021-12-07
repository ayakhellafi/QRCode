import pyqrcode
link="https://www.facebook.com/justine.eva.31/"
url= pyqrcode.create(link)
url.png("khellafiaya.png",scale=6)

