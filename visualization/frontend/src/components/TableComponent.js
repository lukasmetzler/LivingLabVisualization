import React, { useState, useEffect } from "react";
import axios from "axios";
import { useTable, usePagination, useSortBy } from "react-table";

const TableComponent = () => {
  const [data, setData] = useState([]);
  const [pageCount, setPageCount] = useState(0);

  const fetchData = async ({ pageSize, pageIndex }) => {
    const result = await axios.get(
      `http://85.215.59.47/auth/api/dim_zed_body_tracking?pageSize=${pageSize}&page=${
        pageIndex + 1
      }`
    );
    setData(result.data.items);
    setPageCount(result.data.pageCount);
  };

  const columns = React.useMemo(
    () => [
      { Header: "ID", accessor: "zed_body_tracking_id" },
      { Header: "Is New", accessor: "is_new" },
      { Header: "Is Tracked", accessor: "is_tracked" },
      { Header: "Camera Pitch", accessor: "camera_pitch" },
      { Header: "Camera Roll", accessor: "camera_roll" },
      { Header: "Camera Yaw", accessor: "camera_yaw" },
      { Header: "Body List", accessor: "body_list" },
      { Header: "Created At", accessor: "created_at" },
    ],
    []
  );

  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    prepareRow,
    page,
    canPreviousPage,
    canNextPage,
    pageOptions,
    nextPage,
    previousPage,
    setPageSize: updatePageSize,
    state: { pageIndex, pageSize },
  } = useTable(
    {
      columns,
      data,
      initialState: { pageIndex: 0 },
      manualPagination: true,
      pageCount,
      useControlledState: (state) => {
        fetchData({ pageSize: state.pageSize, pageIndex: state.pageIndex });
        return state;
      },
    },
    useSortBy,
    usePagination
  );

  return (
    <div className="p-4 bg-gray-100 dark:bg-gray-900">
      <table
        {...getTableProps()}
        className="min-w-full bg-white dark:bg-gray-800"
      >
        <thead className="bg-gray-200 dark:bg-gray-700">
          {headerGroups.map((headerGroup) => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map((column) => (
                <th
                  {...column.getHeaderProps(column.getSortByToggleProps())}
                  className="px-4 py-2 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider"
                >
                  {column.render("Header")}
                  <span>
                    {column.isSorted
                      ? column.isSortedDesc
                        ? " 🔽"
                        : " 🔼"
                      : ""}
                  </span>
                </th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody {...getTableBodyProps()}>
          {page.map((row) => {
            prepareRow(row);
            return (
              <tr
                {...row.getRowProps()}
                className="bg-white dark:bg-gray-800 border-b dark:border-gray-700"
              >
                {row.cells.map((cell) => {
                  return (
                    <td
                      {...cell.getCellProps()}
                      className="px-4 py-2 whitespace-nowrap text-sm font-medium text-gray-900 dark:text-gray-100"
                    >
                      {cell.render("Cell")}
                    </td>
                  );
                })}
              </tr>
            );
          })}
        </tbody>
      </table>
      <div className="pagination flex items-center justify-between py-3 bg-gray-100 dark:bg-gray-900">
        <button
          onClick={() => previousPage()}
          disabled={!canPreviousPage}
          className="bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-200 py-2 px-4 rounded disabled:opacity-50"
        >
          Previous
        </button>
        <span className="text-gray-700 dark:text-gray-200">
          Page{" "}
          <strong>
            {pageIndex + 1} of {pageOptions.length}
          </strong>{" "}
        </span>
        <button
          onClick={() => nextPage()}
          disabled={!canNextPage}
          className="bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-200 py-2 px-4 rounded disabled:opacity-50"
        >
          Next
        </button>
        <select
          value={pageSize}
          onChange={(e) => updatePageSize(Number(e.target.value))}
          className="ml-4 bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-200 py-2 px-4 rounded"
        >
          {[10, 20, 30, 40, 50].map((size) => (
            <option key={size} value={size}>
              Show {size}
            </option>
          ))}
        </select>
      </div>
    </div>
  );
};

export default TableComponent;
