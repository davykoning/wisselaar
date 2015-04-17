# coding=utf-8
"""
geld wissel programma
Davy Koning
2015
"""


def main():
    """
    start programma
    """
    print("== geld wisselaar ==")
    munten = [200, 100, 50, 20, 10, 5, 2, 1]
    bestandsnaam = input('geef naam van tekstbestand met bedragen: ')
    uitvoerbestandsnaam = input('geef nog een naam van een leeg tekstbestand: ')
    inp = open(bestandsnaam)
    output = open(uitvoerbestandsnaam, 'w')
    for regel in inp.readlines():
        try:
            bedrag = int(regel)
        except ValueError:
            print('ongeldige input, ValueError -> ', regel)
            continue
        opgemaaktbedrag = '%3d:' % bedrag
        betaling = []
        restbedrag = bedrag
        for munt in munten:

            while restbedrag >= munt:
                betaling.append(munt)
                restbedrag -= munt
        assert restbedrag == 0
        printregel = "%s %s" % (opgemaaktbedrag, betaling)
        print(printregel)
        output.write(printregel)
        output.write("\n")


if __name__ == "__main__":
    main()


