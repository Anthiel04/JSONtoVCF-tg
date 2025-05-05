from string import Template

template = Template("The shares of $company have $state. This is $reaction.")
print(template.substitute(state="dropped", company="Google", reaction="bad"))


class VCF:
    def __init__(self, N, FN, TEL, REV):
        self.BEGIN = "BEGIN:VCARD"
        self.VERSION = "VERSION:4.0"
        self.N = "N:" + N
        self.FN = "FN:" + FN
        self.TEL = "TEL;TYPE=HOME,VOICE:" + TEL
        self.REV = "REV:" + REV
        self.END = "END:VCARD"
        self.TEMPLATE = Template(
            """
$BEGIN
$VERSION
$N
$FN
$TEL
$REV
$END
"""
        )

    def getContact(self):
        return self.TEMPLATE.substitute(
            BEGIN=self.BEGIN,
            VERSION=self.VERSION,
            N=self.N,
            FN=self.FN,
            TEL=self.TEL,
            REV=self.REV,
            END=self.END,
        )
