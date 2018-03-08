// test self-loop s0
repeat(3) @(posedge clk); #1;
pbr = 1; pbl = 1;
@(posedge clk); #1;
pbr = 0; pbl = 0;

// test move to s1 from s0
repeat(3) @(posedge clk); #1; 
pbr = 1; pbl = 0;
@(posedge clk); #1;		
pbr = 0; pbl = 0;

// test self-loop s1
repeat(3) @(posedge clk); #1;
pbr = 1; pbl = 1;
@(posedge clk); #1;
pbr = 0; pbl = 0;

// test move to s2 from s1
repeat(3) @(posedge clk); #1; 
pbr = 1; pbl = 0;
@(posedge clk); #1;		
pbr = 0; pbl = 0;

// test self-loop s2
repeat(3) @(posedge clk); #1;
pbr = 1; pbl = 1;
@(posedge clk); #1;
pbr = 0; pbl = 0;

// test move to s3 from s2
repeat(3) @(posedge clk); #1; 
pbr = 1; pbl = 0;
@(posedge clk); #1;		
pbr = 0; pbl = 0;

// test self-loop s3
repeat(3) @(posedge clk); #1;
pbr = 1; pbl = 1;
@(posedge clk); #1;
pbr = 0; pbl = 0;

// test move to s0 from s3
repeat(3) @(posedge clk); #1; 
pbr = 1; pbl = 0;
@(posedge clk); #1;		
pbr = 0; pbl = 0;

// test move to s3 from s0
repeat(3) @(posedge clk); #1; 
pbr = 0; pbl = 1;
@(posedge clk); #1;		
pbr = 0; pbl = 0;

// test move to s2 from s3
repeat(3) @(posedge clk); #1; 
pbr = 0; pbl = 1;
@(posedge clk); #1;		
pbr = 0; pbl = 0;

// test move to s1 from s2
repeat(3) @(posedge clk); #1; 
pbr = 0; pbl = 1;
@(posedge clk); #1;		
pbr = 0; pbl = 0;

// test move to s0 from s1
repeat(3) @(posedge clk); #1; 
pbr = 0; pbl = 1;
@(posedge clk); #1;		
pbr = 0; pbl = 0;