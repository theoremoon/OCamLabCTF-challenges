from Crypto.Util.number import *

p = 104209431158949936402108500402271793045579807456147152224617503958610815865360406026909720891759880964456019955626625800073582972952502829573072093855726415205846918946554591160350490889154150513446260977347790964277519845361905889050313423234014564026286390834362237035513527610760163065614641836814793353647
q = 143829822477093021663840163922351592752048622304801481151138738362786914245391035487502863740174352651831373129866078288419285370532296353990975962961376521046248980709857283190902556563095320013559087965783582549393617516970200001311116498318947210509799871613268795859166110823785491913051735894387012178007
e = 65537
c = 4551485166501576299521441344649219138163467334920944096138199665870424992071756242843371846904346059346674511509868926674426577778237087292519425914081176405465861773458961740472721930150871063947387241468750105776261084854691663828459703558621686297723577447846838552093392387284440615935464481536356004555919252085955246750656039597408118065386109287671572245646733683897050012964729252662021736051623887067721477398400497980795003552598914575102542815089889196398823732783634888925883714442767275331029269529896335191304794529520890886686880859418215346710702772795003556639320435818978485192240805003521861839622

d = inverse(e, (p - 1) * (q - 1))
m = pow(c, d, p * q)
print(bytes.fromhex(hex(m)[2:]))