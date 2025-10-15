import os
import io
import sys
import math
import unittest

BASE_DIR = os.path.dirname(__file__)
os.chdir(BASE_DIR)

_old_stdout = sys.stdout
sys.stdout = io.StringIO()
try:
    from si201_proj1_zuminghu import cal_ave_mass, cal_length_diff
finally:
    sys.stdout = _old_stdout


def dummy_data_for_mass():
    return {
        'species': ['Adelie','Adelie','Chinstrap','Adelie','Gentoo','Adelie'],
        'island':  ['Torgersen','Torgersen','Dream','Biscoe','Torgersen','Torgersen'],
        'bill_length_mm':    [38.9, 41.1, -1, 37.8, 46.2, 39.5],
        'bill_depth_mm':     [17.8, 18.2, 19.5, 18.3, -1, 17.4],
        'flipper_length_mm': [181, 190, 195, -1, 217, 186],
        'body_mass_g':       [3000, 4000, 3700, 3200, -1, -1],
        'sex':               ['male','female','male','female','male','male'],
        'year':              ['2007','2007','2009','2008','2009','2007'],
    }

def dummy_data_for_bill_length():
    return {
        'species': ['Chinstrap','Chinstrap','Adelie','Adelie','Gentoo','Adelie'],
        'island':  ['Dream','Dream','Dream','Biscoe','Dream','Dream'],
        'bill_length_mm':    [42.0, 44.0, 40.0, 39.0, -1, 38.0],
        'bill_depth_mm':     [18.0, 19.0, 18.5, 18.0, 17.5, 18.2],
        'flipper_length_mm': [195, 197, 190, 188, 200, 189],
        'body_mass_g':       [3600, 3700, 3400, 3300, 4500, 3350],
        'sex':               ['male','female','female','female','male','male'],
        'year':              ['2008','2009','2008','2008','2009','2009'],
    }


class TestCalAveMass(unittest.TestCase):
    def test_normal_single_valid(self):
        data = dummy_data_for_mass()
        avg = cal_ave_mass(data)
        self.assertTrue(math.isclose(avg, 3000.0, rel_tol=1e-9))

    def test_normal_multiple_valid(self):
        data = dummy_data_for_mass()
        data['species'].append('Adelie')
        data['island'].append('Torgersen')
        data['bill_length_mm'].append(40.0)
        data['bill_depth_mm'].append(18.0)
        data['flipper_length_mm'].append(185)
        data['body_mass_g'].append(4200)
        data['sex'].append('male')
        data['year'].append('2008')
        avg = cal_ave_mass(data)
        self.assertTrue(math.isclose(avg, 3600.0, rel_tol=1e-9))

    def test_edge_all_missing(self):
        data = dummy_data_for_mass()
        data['body_mass_g'][0] = -1
        avg = cal_ave_mass(data)
        self.assertTrue(math.isclose(avg, 0.0, rel_tol=1e-9))

    def test_edge_no_match(self):
        data = dummy_data_for_mass()
        data['island'] = ['Dream'] * len(data['island'])
        avg = cal_ave_mass(data)
        self.assertTrue(math.isclose(avg, 0.0, rel_tol=1e-9))


class TestCalLengthDiff(unittest.TestCase):
    def test_normal_typical(self):
        data = dummy_data_for_bill_length()
        diff = cal_length_diff(data)
        self.assertTrue(math.isclose(abs(diff), 4.0, rel_tol=1e-9))

    def test_normal_with_noise(self):
        data = dummy_data_for_bill_length()
        data['species'].extend(['Chinstrap', 'Adelie'])
        data['island'].extend(['Biscoe', 'Torgersen'])
        data['bill_length_mm'].extend([50.0, 10.0])
        data['bill_depth_mm'].extend([19.5, 17.0])
        data['flipper_length_mm'].extend([205, 170])
        data['body_mass_g'].extend([3800, 2500])
        data['sex'].extend(['male', 'female'])
        data['year'].extend(['2010', '2010'])
        data['species'].append('Chinstrap')
        data['island'].append('Dream')
        data['bill_length_mm'].append(-1)
        data['bill_depth_mm'].append(18.5)
        data['flipper_length_mm'].append(190)
        data['body_mass_g'].append(3600)
        data['sex'].append('male')
        data['year'].append('2011')
        diff = cal_length_diff(data)
        self.assertTrue(math.isclose(abs(diff), 4.0, rel_tol=1e-9))

    def test_edge_missing_species(self):
        data = dummy_data_for_bill_length()
        for i in range(len(data['species'])-1, -1, -1):
            if data['island'][i] == 'Dream' and data['species'][i] == 'Adelie':
                for k in list(data.keys()):
                    del data[k][i]
        diff = cal_length_diff(data)
        self.assertTrue(math.isclose(diff, 0.0, rel_tol=1e-9))

    def test_edge_all_missing_values(self):
        data = dummy_data_for_bill_length()
        for i in range(len(data['species'])):
            if data['island'][i] == 'Dream':
                data['bill_length_mm'][i] = -1
        diff = cal_length_diff(data)
        self.assertTrue(math.isclose(diff, 0.0, rel_tol=1e-9))


if __name__ == '__main__':
    unittest.main()