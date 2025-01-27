# fortitudo.tech - Novel Investment Technologies.
# Copyright (C) 2021-2022 Fortitudo Technologies.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from context import np, load_parameters, time_series, R


def test_load_data():
    instrument_names, means, covariance_matrix = load_parameters()
    assert list(R.columns) == instrument_names
    I = R.shape[1]
    assert means.shape == (I,)
    assert covariance_matrix.shape == (I, I)


def test_time_series():
    assert time_series.shape == (5040, 79)
    assert np.all(time_series.values >= 0)
