const express = require("express");
const db = require("../db");
const router = express.Router();

router.get("/dim_zed_body_tracking", async (req, res) => {
  const {
    page = 1,
    pageSize = 10,
    sortBy = "created_at",
    sortOrder = "asc",
  } = req.query;

  try {
    const offset = (page - 1) * pageSize;

    // Count the total number of rows
    const totalCountResult = await db.one(
      "SELECT COUNT(*) FROM dim_zed_body_tracking_1og_r1"
    );
    const totalCount = parseInt(totalCountResult.count, 10);

    // Fetch the data with pagination and sorting
    const data = await db.any(
      `SELECT * FROM dim_zed_body_tracking_1og_r1 ORDER BY ${sortBy} ${sortOrder} LIMIT $1 OFFSET $2`,
      [pageSize, offset]
    );

    res.json({
      items: data,
      pageCount: Math.ceil(totalCount / pageSize),
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
