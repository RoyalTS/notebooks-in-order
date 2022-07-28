import nbformat as nbf
import argparse
import sys


def check_execution_order(
    notebook_path,
    check_all_executed=True,
    check_top_to_bottom=True,
    check_in_order=True,
):
    ntbk = nbf.read(notebook_path, nbf.NO_CONVERT)

    # extract all code cells (disregard markdown, raw and others), the extract the execution order
    output_cells = [cell for cell in ntbk.cells if cell["cell_type"] == "code"]
    # remove empty cells
    non_empty_cells = [cell for cell in output_cells if cell["source"] != ""]
    execution_counts = [cell["execution_count"] for cell in non_empty_cells]

    pass_check = [True]

    def _check_all_executed(execution_counts: list) -> bool:
        """Check all cells were executed.

        Parameters
        ----------
        execution_counts : list
            execution_counts

        Returns
        -------
        bool
        """
        return not None in execution_counts

    def _check_in_order(execution_counts: list) -> bool:
        """Check that execution counts that aren't None go from 1 to N.

        Parameters
        ----------
        execution_counts : list
            execution counts

        Returns
        -------
        bool
        """
        execution_counts = [x for x in execution_counts if x is not None]
        return [x + 1 for x in range(len(execution_counts))] == execution_counts

    if check_in_order:
        pass_check.append(_check_in_order(execution_counts))

    if check_all_executed:
        pass_check.append(_check_all_executed(execution_counts))

    if check_top_to_bottom:
        pass_check.append(
            _check_all_executed(execution_counts) and _check_in_order(execution_counts)
        )

    return all(pass_check)


def check_all_notebooks(filenames: list) -> bool:
    """Check whether all notebooks in the given list were run top to bottom.

    Parameters
    ----------
    filenames : list
        list of notebook filenames

    Returns
    -------
    bool
    """
    check_results = {
        f: check_execution_order(f, check_top_to_bottom=True) for f in filenames
    }

    for f, pass_check in check_results.items():
        if not pass_check:
            print(f"Notebook {f} not executed top to bottom!")

    # if any of the notebooks don't pass checks, exit with error code 1
    return all(check_results.values())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    if not check_all_notebooks(args.filenames):
        sys.exit(1)


if __name__ == "__main__":
    main()
