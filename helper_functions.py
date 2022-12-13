from collections import namedtuple
from typing import Dict, List, Tuple
import pandas as pd

GffEntry = namedtuple(
    "GffEntry",
    [
        "seqname",
        "source",
        "feature",
        "start",
        "end",
        "score",
        "strand",
        "frame",
        "attribute",
    ],
)


GeneDict = Dict[str, GffEntry]


def read_gff(fname: str) -> Dict[str, GffEntry]:
    gene_dict = {}

    with open(fname) as f:
        for line in f:
            if line.startswith("#"):  # Comments start with '#' character
                continue

            parts = line.split("\t")
            parts = [p.strip() for p in parts]

            # Convert start and stop to ints
            start_idx = GffEntry._fields.index("start")
            parts[start_idx] = int(parts[start_idx]) - 1  # GFFs count from 1..
            stop_idx = GffEntry._fields.index("end")
            parts[stop_idx] = int(parts[stop_idx]) - 1  # GFFs count from 1..

            # Split the attributes
            attr_index = GffEntry._fields.index("attribute")
            attributes = {}
            for attr in parts[attr_index].split(";"):
                attr = attr.strip()
                k, v = attr.split("=")
                attributes[k] = v
            parts[attr_index] = attributes

            entry = GffEntry(*parts)

            gene_dict[entry.attribute["gene_name"]] = entry

    return gene_dict


def split_read(read: str) -> Tuple[str, str]:
    """Split a given read into its barcode and DNA sequence. The reads are
    already in DNA format, so no additional work will have to be done. This
    function needs only to take the read, and split it into the cell barcode,
    the primer, and the DNA sequence. The primer is not important, so we discard
    that.

    The first 12 bases correspond to the cell barcode.
    The next 24 bases corresond to the oligo-dT primer. (discard this)
    The reamining bases corresond to the actual DNA of interest.

    Parameters
    ----------
    read: str

    Returns
    -------
    str: cell_barcode
    str: mRNA sequence

    """
    raise NotImplementedError()


def map_read_to_gene(read: str, ref_seq: str, genes: GeneDict) -> Tuple[str, float]:
    """Map a given read to a gene with a confidence score using Hamming distance.

    Parameters
    ----------
    read: str
        The DNA sequence to be aligned to the reference sequence. This should
        NOT include the cell barcode or the oligo-dT primer.
    ref_seq: str
        The reference sequence that the read should be aligned against.
    genes: GeneDict

    Returns
    -------
    gene: str
        The name of the gene (using the keys of the `genes` parameter, which the
        read maps to best. If the best alignment maps to a region that is not a
        gene, the function should return `None`.
    similarity: float
        The similarity of the aligned read. This is computed by taking the
        Hamming distance between the aligned read and the reference sequence.
        E.g. catac and cat-x will have similarity 3/5=0.6.


    """
    raise NotImplementedError()


def generate_count_matrix(
    reads: List[str], ref_seq: str, genes: GeneDict, similarity_threshold: float
) -> pd.DataFrame:
    """

    Parameters
    ----------
    reads: List[str]
        The list of all reads that will be aligned.
    ref_seq: str
        The reference sequence that the read should be aligned against.
    genes: GeneDict
    similarity_threshold: float

    Returns
    -------
    count_table: pd.DataFrame
        The count table should be an N x G matrix where N is the number of
        unique cell barcodes in the reads and G is the number of genes in
        `genes`. The dataframe columns should be to a list of strings
        corrsponding to genes and the dataframe index should be a list of
        strings corresponding to cell barcodes. Each cell in the matrix should
        indicate the number of times a read mapped to a gene in that particular
        cell.

    """
    raise NotImplementedError()


def filter_matrix(
    count_matrix: pd.DataFrame,
    min_counts_per_cell: float,
    min_counts_per_gene: float,
) -> pd.DataFrame:
    """Filter a matrix by cell counts and gene counts.
    The cell count is the total number of molecules sequenced for a particular
    cell. The gene count is the total number of molecules sequenced that
    correspond to a particular gene. Filtering statistics should be computed on
    the original matrix. E.g. if you filter out the genes first, the filtered
    gene molecules should still count towards the cell counts.

    Parameters
    ----------
    count_matrix: pd.DataFrame
    min_counts_per_cell: float
    min_counts_per_gene: float

    Returns
    -------
    filtered_count_matrix: pd.DataFrame

    """
    raise NotImplementedError()


def normalize_expressions(expression_data: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize expressions by applying natural log-transformation with pseudo count 1,
    and scaling expressions of each sample to sum up to 10000.

    Parameters
    ----------
    expression_data: pd.DataFrame
        Expression matrix with cells as rows and genes as columns.

    Returns
    -------
    normalized_data: pd.DataFrame
        Normalized expression matrix with cells as rows and genes as columns.
        Matrix should have the same shape as the input matrix.
        Matrix should have the same index and column labels as the input matrix.
        Order of rows and columns should remain the same.
        Values in the matrix should be positive or zero.
    """
    raise NotImplementedError()


def hypergeometric_pval(N: int, n: int, K: int, k: int) -> float:
    """
    Calculate the p-value using the following hypergeometric distribution.

    Parameters
    ----------
    N: int
        Total number of genes in the study (gene expression matrix)
    n: int
        Number of genes in your proposed gene set (e.g. from differential expression)
    K: int
        Number of genes in an annotated gene set (e.g. GO gene set)
    k: int
        Number of genes in both annotated and proposed geneset

    Returns
    -------
    p_value: float
        p-value from hypergeometric distribution of finding such or
        more extreme match at random
    """
    raise NotImplementedError()
