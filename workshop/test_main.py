import pandas as pd
import main

# Test Drop Notes

def test_drop_notes_column_dropped():
    # Create a sample DataFrame with 'notes' column
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'notes': ['note1', 'note2', 'note3']})

    # Call the drop_notes function and assign the result
    df = main.drop_notes(df)

    # Assert that 'notes' column is dropped
    columns = df.columns.to_list()
    assert columns == ['A', 'B']
    
    
def test_drop_notes_columns_present():
    # Create a sample DataFrame with 'notes' column
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'notes': ['note1', 'note2', 'note3']})

    # Call the drop_notes function
    result = main.drop_notes(df)

    # Assert that other columns are still present
    assert 'A' in result.columns
    assert 'B' in result.columns


def test_drop_notes_dataframe_unchanged():
    # Create a sample DataFrame with 'notes' column
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'notes': ['note1', 'note2', 'note3']})

    # Call the drop_notes function
    result = main.drop_notes(df)

    # Assert that the shape of the DataFrame is unchanged
    assert result.shape == (3, 2)

    # Assert that the original DataFrame is not modified
    assert 'notes' in df.columns
    assert df.shape == (3, 3)


# Test Remove Lines

def test_remove_newlines_carriage_returns():
        
    # Create a sample DataFrame with string columns containing newlines and carriage returns
    df = pd.DataFrame({'A': ['Hello\nWorld', 'Foo\rBar'], 'B': ['Lorem\nIpsum', 'Dolor\rSit']})

    # Call the remove_newlines_carriage_returns function
    result = main.remove_newlines_carriage_returns(df)

    # Assert that newlines and carriage returns are removed from string columns
    assert result['A'].tolist() == ['Hello World', 'Foo Bar']
    assert result['B'].tolist() == ['Lorem Ipsum', 'Dolor Sit']

    # Assert that other columns remain unchanged
    assert 'A' in result.columns
    assert 'B' in result.columns

def test_remove_newlines_columns_unchanged():
    # Create a sample DataFrame with string columns containing newlines and carriage returns
    df = pd.DataFrame({'A': ['Hello\nWorld', 'Foo\rBar'], 'B': ['Lorem\nIpsum', 'Dolor\rSit']})

    # Call the remove_newlines_carriage_returns function
    result = main.remove_newlines_carriage_returns(df)

    # Assert that the original DataFrame is not modified
    assert 'A' in df.columns
    assert 'B' in df.columns
    assert df.shape == (2, 2)

def test_remove_newlines_shape_is_unchanged():
    # Create a sample DataFrame with string columns containing newlines and carriage returns
    df = pd.DataFrame({'A': ['Hello\nWorld', 'Foo\rBar'], 'B': ['Lorem\nIpsum', 'Dolor\rSit']})

    # Call the remove_newlines_carriage_returns function
    result = main.remove_newlines_carriage_returns(df)

    # Assert that the shape of the DataFrame is unchanged
    assert result.shape == (2, 2)
    def test_drop_and_one_hot_encode_red_wine_creates_column_and_drops_variety():
        # Create a DataFrame with 'variety' column
        df = pd.DataFrame({'variety': ['Red Wine', 'White Wine', 'Red Wine'], 'rating': [91, 88, 95]})
        result = main.drop_and_one_hot_encode_red_wine(df)
        # Check that 'Red_Wine' column exists and 'variety' is dropped
        assert 'Red_Wine' in result.columns
        assert 'variety' not in result.columns
        # Check correct encoding
        assert result['Red_Wine'].tolist() == [1, 0, 1]

    def test_drop_and_one_hot_encode_red_wine_no_variety_column():
        # DataFrame without 'variety' column
        df = pd.DataFrame({'rating': [91, 88, 95]})
        result = main.drop_and_one_hot_encode_red_wine(df)
        # Should not add 'Red_Wine' column
        assert 'Red_Wine' not in result.columns
        assert 'rating' in result.columns

    def test_drop_and_one_hot_encode_red_wine_dataframe_shape():
        # DataFrame with 'variety' column
        df = pd.DataFrame({'variety': ['Red Wine', 'White Wine'], 'rating': [90, 85]})
        result = main.drop_and_one_hot_encode_red_wine(df)
        # Should have same number of rows, one less column (variety dropped, Red_Wine added)
        assert result.shape == (2, 2)

    def test_drop_and_one_hot_encode_red_wine_original_dataframe_unchanged():
        # DataFrame with 'variety' column
        df = pd.DataFrame({'variety': ['Red Wine', 'White Wine'], 'rating': [90, 85]})
        df_copy = df.copy()
        main.drop_and_one_hot_encode_red_wine(df)
        # Original DataFrame should not be modified
        assert df.equals(df_copy)
