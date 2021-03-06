__author__ = 'aditya'

from tex import *
from datetime import datetime
import copy, os


will = r"""\documentclass{article}

\usepackage{graphicx}

\oddsidemargin=0.0in

\evensidemargin=0in

\textwidth=6.5in

\marginparwidth=0.5in

\headheight=0pt

\headsep=0pt

\textheight=9.0in

\newcommand\textbox[1]{%

\parbox{.950\textwidth}{#1}%

}

\begin{document}

%--------------------------------------------------------------------------------------------------------------------------------------------------------------
.

\vspace{2.5in}

\centerline{\huge \textbf{Last Will Testament}}

\vspace{0.5in}

\noindent \textbox{\large I, \#name\#, son/wife of \#dependent\#, resident of: \#address\#, age \#age\# years, am making this will on the day of \#date\# out of my free volition and without any coercion or undue influence whatsoever; and state that this is my last will and that I hereby revoke all wills and codicil made by me at any time heretoforce, I bequeath my property, interests and other rights as follows.}

\vspace{0.3in}

\noindent \textbox{\large I am the sole and absolute owner of diverse other assets and properties movable and immovable held by me including shares, bonds, deposits, jewellery, silver utensils and household goods and no one else has any shares right, title, interest, claim or demand whatsoever into or against the same. I thus have full right and absolute power and complete authority to make this my last Will and Testament in respect thereof and any other property or assets, movable and immovable which may be substituted in their place or may come into my possession in future.}

\vspace{0.3in}

\noindent \textbox{\large I hereby direct the Executors that after my death they shall collect and take possession of all the aforesaid properties and assets whatsoever and wheresoever situate and they shall recover all outstanding due to me and pay out of my assets all my debts, if any, estate duty leviable in respect of the gifts made by me during my life time which may be included in my dutiable estate and the assets and other taxes and testamentary expenses and to deal with my residuary estate in the manner hereinafter directed.}

\vspace{0.3in}

\noindent \textbox{\large I declare that the amounts covered by the insurances policies on my life which have already been assigned or in respect of which nominations have already been made by me earlier shall belong to the assignee/nominee absolutely.}

\vspace{0.3in}

\#props\#

\#jewels\#

\end{document}
""".decode('utf-8')

prop = r"""
\textbox{\large $\bullet$ \large I bequeath on my death to \#benefactor\# ,my title interests and all other rights which I have as owner of the \#rescom\# Property at \#propaddress\# , I hereby sate that he shall been titled to use and enjoy the said property at his own will after my death.}
\vspace{0.3in}

""".decode('utf-8')

jewel = r"""
\textbox{\large $\bullet$ \large I bequeath on my death the following ornaments and jewellery belonging to me to \#jewname\#: \#description\#}
\vspace{0.3in}
\begin{figure}[ht!]
\centering
\includegraphics[width=90mm]{\#imgpath\#}
\caption{A simple caption}
\label{overflow}
\end{figure}
""".decode('utf-8')

def check(feed):
    if '\\' in feed:
        feed = feed.replace('\\', '')
    # if '^' in feed:
    #     feed = feed.replace('\\', '\\textasciicircum{}')
    # if '~' in feed:
    #     feed = feed.replace('\\', '\\textasciicitilde{}')
    for x in ['#', '-', '%', '$', '&', '_', '{', '}']:
        feed = feed.replace(x, '\\' + x)
    if '\n' in feed:
        feed = feed.replace('\n', '\\\\')
    if '\n' in feed:
        feed = feed.replace('\r', ' ')
    print feed
    return feed

def fillin(d):
    global will
    global prop
    global jewel
    will = copy.deepcopy(will)
    will = will.replace("\#name\#", check(d['name']))
    will = will.replace("\#dependent\#", check(d['dependent']))
    will = will.replace("\#address\#", check(d['address']))
    will = will.replace("\#age\#", check(d['age']))
    will = will.replace("\#date\#", datetime.now().strftime(format("%A, %dth of %B, %Y")))

    propsfil = r""" """
    if len(d['properties']):
        propsfil += r"""\noindent \textbox{\Large \textbf{Properties}}
        """
        for i in range(len(d['properties'])):
            propin = d['properties'][i+1]
            proptemp = copy.deepcopy(prop)
            proptemp = proptemp.replace("\#benefactor\#", check(propin['beneficiary']))
            if propin['type'] == u'res':
                proptemp = proptemp.replace("\#rescom\#", ur"residential")
            else:
                proptemp = proptemp.replace("\#rescom\#", ur"commercial")
            proptemp = proptemp.replace("\#propaddress\#", check(propin['address']))
            propsfil += proptemp
    print propsfil
    will = will.replace("\#props\#", propsfil)

    jewfil = r""" """
    if len(d['jewels']):
        jewfil += r"""\noindent \textbox{\Large \textbf{Jewellery}}
                \vspace{0.3in}"""

        for i in range(len(d['jewels'])):
            jewin = d['jewels'][i+1]
            jewtemp = copy.deepcopy(jewel)
            jewtemp = jewtemp.replace("\#jewname\#", check(jewin['beneficiary']))
            jewtemp = jewtemp.replace("\#description\#", check(jewin['description']))
            jewtemp = jewtemp.replace("\#imgpath\#", check(os.path.abspath(jewin['file_path'])))
            jewfil += jewtemp
        print jewfil
    will = will.replace("\#jewels\#", jewfil)

    return latex2pdf(will)

