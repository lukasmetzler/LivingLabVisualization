import React, { useState, useEffect } from "react";
import axios from "axios";
import { useTable, usePagination, useSortBy } from "react-table";

const TableComponent = () => {
  const [data, setData] = useState([]);
  const [pageCount, setPageCount] = useState(0);

  const fetchData = async ({ pageSize, pageIndex }) => {
    const result = await axios.get(
      `http://85.215.59.47/api/dim_zed_body_tracking?pageSize=${pageSize}&page=${
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
    <div>
      <table {...getTableProps()} className="min-w-full bg-white">
        <thead>
          {headerGroups.map((headerGroup) => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map((column) => (
                <th {...column.getHeaderProps(column.getSortByToggleProps())}>
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
              <tr {...row.getRowProps()}>
                {row.cells.map((cell) => {
                  return (
                    <td {...cell.getCellProps()}>{cell.render("Cell")}</td>
                  );
                })}
              </tr>
            );
          })}
        </tbody>
      </table>
      <div className="pagination">
        <button onClick={() => previousPage()} disabled={!canPreviousPage}>
          Previous
        </button>
        <span>
          Page{" "}
          <strong>
            {pageIndex + 1} of {pageOptions.length}
          </strong>{" "}
        </span>
        <button onClick={() => nextPage()} disabled={!canNextPage}>
          Next
        </button>
        <select
          value={pageSize}
          onChange={(e) => updatePageSize(Number(e.target.value))}
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
