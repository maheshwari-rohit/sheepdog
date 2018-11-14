import os

from sheepdog.utils.transforms import TSVToJSONConverter


def test_tsv_submission_handle_array_type():
    """
    When submitting a TSV file, array fields should be converted to lists.
    """

    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/experimental_metadata.tsv')
    doc = None
    with open(file_path, 'r') as f:
        doc = f.read()
    assert doc

    data, errors = TSVToJSONConverter().convert(doc)
    assert data
    assert not errors

    for row in data:
        # make sure the array is handled properly
        array = row['array_field']
        assert isinstance(array, list)
        assert len(array) > 0