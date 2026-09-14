import sys, unittest
from md import calcenergy

from asap3 import EMT
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution


class MdTests(unittest.TestCase):
    def test_calcenergy(self):
        size = 3
        #Crystal
        atoms = FaceCenteredCubic(
                directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                symbol='Cu',
                size=(size, size, size),
                pbc=True,
            )
        # Describe the interatomic interactions with the Effective Medium Theory
        atoms.calc = EMT()

        # Set the momenta corresponding to T=300K
        MaxwellBoltzmannDistribution(atoms, temperature_K=300)

        epot, ekin, etot, temp = calcenergy(atoms)

        self.assertAlmostEqual(etot, epot + ekin)
        print(
                    'Energy per atom: Calculated Etot = %.3feV  Real Etot = %.3feV (T=%3.0fK)  '
                    % (epot + ekin, etot, temp)
                )
        

if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())

