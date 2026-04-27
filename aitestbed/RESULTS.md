# 6G AI Traffic Characterization Testbed - Test Results

Generated: 2026-04-27 19:07:35
Test Duration: 40 minutes

## Test Summary

| Metric | Value |
|--------|-------|
| Total Records | 693 |
| Scenarios Tested | 1 |
| Network Profiles | 10 |
| Success Rate | 100.0% |
| Run Selection | latest per scenario (gap > 300s) |

## Scenarios Tested

| Scenario | Runs | Success Rate | Avg Latency (s) |
|----------|------|--------------|-----------------|
| Realtime Audio WebRTC - Provider A | 693 | 100.0 | 3.11 |

## Network Profiles Used

| Profile | Description |
|---------|-------------|
| ideal_6g | 1ms delay, 0% loss, unlimited BW (baseline) |
| 5g_urban | 20ms delay, 0.1% loss, 100Mbit |
| wifi_good | 30ms delay, 0.1% loss, 50Mbit |
| cell_edge | 120ms delay, 1% loss, 5Mbit |
| satellite | 600ms delay, 0.5% loss, 10Mbit |
| congested | 200ms delay, 3% loss, 1Mbit |
| 5qi_7 | 100ms delay, 0.1% loss (Voice/Live Streaming) |
| 5qi_80 | 10ms delay, 0.0001% loss (Low-latency eMBB/AR) |

## Detailed Results by Scenario and Profile

| Scenario | Profile | Runs | Success | Avg Latency (s) | Min (s) | Max (s) |
|----------|---------|------|---------|-----------------|---------|---------|
| Realtime Audio WebRTC - Provider A | 5g_urban | 70 | 100.0% | 2.546 | 1.194 | 5.071 |
| Realtime Audio WebRTC - Provider A | 5qi_7 | 70 | 100.0% | 2.918 | 1.251 | 6.726 |
| Realtime Audio WebRTC - Provider A | 5qi_80 | 70 | 100.0% | 2.21 | 1.157 | 4.758 |
| Realtime Audio WebRTC - Provider A | 6g_itu_hrllc | 70 | 100.0% | 2.263 | 1.002 | 4.874 |
| Realtime Audio WebRTC - Provider A | cell_edge | 70 | 100.0% | 3.943 | 1.552 | 15.752 |
| Realtime Audio WebRTC - Provider A | congested | 63 | 100.0% | 5.057 | 1.614 | 21.643 |
| Realtime Audio WebRTC - Provider A | no_emulation | 70 | 100.0% | 2.307 | 0.992 | 7.805 |
| Realtime Audio WebRTC - Provider A | satellite_geo | 70 | 100.0% | 4.919 | 1.412 | 13.535 |
| Realtime Audio WebRTC - Provider A | satellite_leo | 70 | 100.0% | 2.6 | 1.152 | 5.227 |
| Realtime Audio WebRTC - Provider A | wifi_good | 70 | 100.0% | 2.53 | 1.143 | 5.388 |

## Time to First Token (TTFT)

| Scenario | Profile | Avg TTFT (s) | Min (s) | Max (s) |
|----------|---------|--------------|---------|---------|
| Realtime Audio WebRTC - Provider A | 5g_urban | 1.697 | 1.112 | 2.425 |
| Realtime Audio WebRTC - Provider A | 5qi_7 | 1.722 | 1.209 | 2.429 |
| Realtime Audio WebRTC - Provider A | 5qi_80 | 1.733 | 1.115 | 2.428 |
| Realtime Audio WebRTC - Provider A | 6g_itu_hrllc | 1.722 | 1.118 | 2.44 |
| Realtime Audio WebRTC - Provider A | cell_edge | 1.753 | 1.113 | 2.451 |
| Realtime Audio WebRTC - Provider A | congested | 1.753 | 1.211 | 2.457 |
| Realtime Audio WebRTC - Provider A | no_emulation | 1.723 | 1.006 | 2.439 |
| Realtime Audio WebRTC - Provider A | satellite_geo | 1.728 | 1.108 | 2.464 |
| Realtime Audio WebRTC - Provider A | satellite_leo | 1.707 | 1.129 | 2.425 |
| Realtime Audio WebRTC - Provider A | wifi_good | 1.699 | 1.119 | 2.421 |

## Bandwidth Usage

| Scenario | Avg Request (bytes) | Avg Response (bytes) | Asymmetry Ratio |
|----------|---------------------|----------------------|-----------------|
| Realtime Audio WebRTC - Provider A | 36612 | 69459 | 2:1 |

## SDP Offer/Answer Samples (WebRTC)

Latest offer/answer pair captured during realtime WebRTC sessions for Realtime Audio WebRTC - Provider A from `logs/sdp/`.

**Offer:** `logs/sdp/20260427_190634_68521b1c_offer.sdp` (2719 bytes)
```sdp
v=0
o=- 3986276793 3986276793 IN IP4 0.0.0.0
s=-
t=0 0
a=group:BUNDLE 0 1
a=msid-semantic:WMS *
m=audio 49243 UDP/TLS/RTP/SAVPF 96 0 8
c=IN IP4 172.18.20.254
a=sendrecv
a=extmap:1 urn:ietf:params:rtp-hdrext:sdes:mid
a=extmap:2 urn:ietf:params:rtp-hdrext:ssrc-audio-level
a=mid:0
a=msid:b3d02d50-72ff-4fe6-badc-2f94b55ffc14 109c9c51-d00b-4986-a8db-07dece6faf3f
a=rtcp:9 IN IP4 0.0.0.0
a=rtcp-mux
a=ssrc:974120550 cname:88897817-5559-4ce6-aa39-4d429dfa6dbf
a=rtpmap:96 opus/48000/2
a=rtpmap:0 PCMU/8000
a=rtpmap:8 PCMA/8000
a=candidate:a8ff4d6977d53ca1a474d2c8346e8e9c 1 udp 2130706431 172.18.20.254 49243 typ host
a=candidate:8f5babcd1d537799d1af29a0c6c869ff 1 udp 2130706431 10.255.0.1 56285 typ host
a=candidate:201b79c7bba7c46b5e109b3cff1d2ae3 1 udp 1694498815 47.250.139.162 49243 typ srflx raddr 172.18.20.254 rport 49243
a=candidate:c1b2740b2e4969c25d836ea2496cfad6 1 udp 1694498815 47.250.139.162 56285 typ srflx raddr 10.255.0.1 rport 56285
a=end-of-candidates
a=ice-ufrag:Cc1G
a=ice-pwd:v5CTKe8rReZlFE0J6RKo6N
a=fingerprint:sha-256 2E:96:AB:7B:FB:31:E1:69:04:77:64:96:3B:01:B5:6F:55:C4:40:DE:82:B0:99:B7:6A:D8:AC:15:F5:69:81:37
a=fingerprint:sha-384 61:9F:55:0B:7D:39:49:F8:0A:6C:3E:29:73:EE:2A:32:E4:8B:20:B9:1A:54:76:95:18:A4:6C:97:79:F9:07:6E:B5:3E:77:90:14:43:19:E2:61:AB:B3:9C:92:BD:FD:3D
a=fingerprint:sha-512 40:E1:33:EB:40:81:D5:D7:2C:9C:C4:1C:F3:D5:E6:97:5C:0C:C1:79:A7:34:9A:B3:29:37:66:C7:28:3A:4A:2D:C0:5E:C6:19:EF:95:3D:5C:F7:6E:95:B0:DA:F6:9A:43:69:FB:FD:D2:BE:B0:94:27:E3:36:6C:EB:F0:5E:13:B6
a=setup:actpass
m=application 56097 DTLS/SCTP 5000
c=IN IP4 172.18.20.254
a=mid:1
a=sctpmap:5000 webrtc-datachannel 65535
a=max-message-size:65536
a=candidate:a8ff4d6977d53ca1a474d2c8346e8e9c 1 udp 2130706431 172.18.20.254 56097 typ host
a=candidate:8f5babcd1d537799d1af29a0c6c869ff 1 udp 2130706431 10.255.0.1 39353 typ host
a=candidate:201b79c7bba7c46b5e109b3cff1d2ae3 1 udp 1694498815 47.250.139.162 56097 typ srflx raddr 172.18.20.254 rport 56097
a=candidate:c1b2740b2e4969c25d836ea2496cfad6 1 udp 1694498815 47.250.139.162 39353 typ srflx raddr 10.255.0.1 rport 39353
a=end-of-candidates
a=ice-ufrag:1wOl
a=ice-pwd:ALECNG4kduuRDwfYmIYZNm
a=fingerprint:sha-256 2E:96:AB:7B:FB:31:E1:69:04:77:64:96:3B:01:B5:6F:55:C4:40:DE:82:B0:99:B7:6A:D8:AC:15:F5:69:81:37
a=fingerprint:sha-384 61:9F:55:0B:7D:39:49:F8:0A:6C:3E:29:73:EE:2A:32:E4:8B:20:B9:1A:54:76:95:18:A4:6C:97:79:F9:07:6E:B5:3E:77:90:14:43:19:E2:61:AB:B3:9C:92:BD:FD:3D
a=fingerprint:sha-512 40:E1:33:EB:40:81:D5:D7:2C:9C:C4:1C:F3:D5:E6:97:5C:0C:C1:79:A7:34:9A:B3:29:37:66:C7:28:3A:4A:2D:C0:5E:C6:19:EF:95:3D:5C:F7:6E:95:B0:DA:F6:9A:43:69:FB:FD:D2:BE:B0:94:27:E3:36:6C:EB:F0:5E:13:B6
a=setup:actpass
```

**Answer:** `logs/sdp/20260427_190634_68521b1c_answer.sdp` (1534 bytes)
```sdp
v=0
o=- 7075162086859809594 1777287993 IN IP4 0.0.0.0
s=-
t=0 0
a=msid-semantic:WMS *
a=fingerprint:sha-256 AE:7A:F2:2C:EA:BA:31:FF:49:65:2F:5A:B6:C6:B9:73:34:44:83:5D:C0:A1:D2:60:EE:41:85:6C:58:4E:4A:67
a=ice-lite
a=group:BUNDLE 0 1
m=audio 9 UDP/TLS/RTP/SAVPF 96 0 8
c=IN IP4 0.0.0.0
a=setup:active
a=mid:0
a=ice-ufrag:hcFtUn/u7/3oNQFw
a=ice-pwd:00m4X2bznsintgaj6Zfs82tdXXJN5EhP
a=rtcp-mux
a=rtcp-rsize
a=rtpmap:96 opus/48000/2
a=fmtp:96 minptime=10;useinbandfec=1
a=rtpmap:0 PCMU/8000
a=rtpmap:8 PCMA/8000
a=ssrc:4176682926 cname:realtimeapi
a=ssrc:4176682926 msid:realtimeapi audio
a=ssrc:4176682926 mslabel:realtimeapi
a=ssrc:4176682926 label:audio
a=msid:realtimeapi audio
a=sendrecv
a=candidate:657706698 1 udp 2130706431 20.184.36.134 3478 typ host ufrag hcFtUn/u7/3oNQFw
a=candidate:1561877326 1 tcp 1671430143 20.184.36.134 443 typ host tcptype passive ufrag hcFtUn/u7/3oNQFw
a=candidate:1972146710 1 udp 2130706431 13.71.25.29 3478 typ host ufrag hcFtUn/u7/3oNQFw
a=candidate:1314481154 1 tcp 1671430143 13.71.25.29 443 typ host tcptype passive ufrag hcFtUn/u7/3oNQFw
a=candidate:256115859 1 udp 2130706431 4.217.235.100 3478 typ host ufrag hcFtUn/u7/3oNQFw
a=candidate:558362903 1 tcp 1671430143 4.217.235.100 443 typ host tcptype passive ufrag hcFtUn/u7/3oNQFw
m=application 9 UDP/DTLS/SCTP webrtc-datachannel
c=IN IP4 0.0.0.0
a=setup:active
a=mid:1
a=sendrecv
a=sctp-port:5000
a=max-message-size:1073741823
a=ice-ufrag:hcFtUn/u7/3oNQFw
a=ice-pwd:00m4X2bznsintgaj6Zfs82tdXXJN5EhP
```

## Charts

### Latency Distribution
![Latency Distribution](results/reports/figures/latency_by_scenario.png)

### Time to First Token (TTFT)
![Time to First Token (TTFT)](results/reports/figures/ttft_by_scenario.png)

### Latency Breakdown (TTFT vs Generation)
![Latency Breakdown (TTFT vs Generation)](results/reports/figures/latency_breakdown.png)

### Bandwidth Asymmetry (UL/DL)
![Bandwidth Asymmetry (UL/DL)](results/reports/figures/bandwidth_asymmetry.png)

### Throughput
![Throughput](results/reports/figures/throughput_by_scenario.png)

### Throughput Over Time
![Throughput Over Time](results/reports/figures/throughput_over_time.png)

### Traffic Burstiness (Per-Request Throughput)
![Traffic Burstiness (Per-Request Throughput)](results/reports/figures/throughput_burstiness.png)

### Token Counts
![Token Counts](results/reports/figures/token_counts.png)

### Token Throughput
![Token Throughput](results/reports/figures/token_throughput.png)

### Token Rate by Profile
![Token Rate by Profile](results/reports/figures/token_rate_by_profile.png)

### Success Rate
![Success Rate](results/reports/figures/success_rate.png)

### Success vs Latency
![Success vs Latency](results/reports/figures/success_vs_latency.png)

### Latency by Network Profile
![Latency by Network Profile](results/reports/figures/latency_by_profile.png)

### Latency Heatmap (Scenario × Profile)
![Latency Heatmap (Scenario × Profile)](results/reports/figures/latency_heatmap.png)

### TTFT Heatmap (Scenario × Profile)
![TTFT Heatmap (Scenario × Profile)](results/reports/figures/ttft_heatmap.png)

### TTFT vs Latency
![TTFT vs Latency](results/reports/figures/ttft_vs_latency.png)

### Degradation Heatmap
![Degradation Heatmap](results/reports/figures/degradation_heatmap.png)

### Streaming Metrics
![Streaming Metrics](results/reports/figures/streaming_metrics.png)

### Protocol Comparison
![Protocol Comparison](results/reports/figures/protocol_comparison.png)

### Data Volume
![Data Volume](results/reports/figures/data_volume.png)

### Request/Response Scatter
![Request/Response Scatter](results/reports/figures/request_response_scatter.png)

### Context Growth
![Context Growth](results/reports/figures/context_growth.png)

### Inter-Turn Idle Time
![Inter-Turn Idle Time](results/reports/figures/inter_turn_idle.png)

### MCP Efficiency
![MCP Efficiency](results/reports/figures/mcp_efficiency.png)

### MCP Latency Breakdown
![MCP Latency Breakdown](results/reports/figures/mcp_latency_breakdown.png)

### MCP Loop Factor by Profile
![MCP Loop Factor by Profile](results/reports/figures/mcp_loop_factor_by_profile.png)

### Pcap RTT Analysis
![Pcap RTT Analysis](results/reports/figures/pcap_rtt_analysis.png)

### Pcap Throughput
![Pcap Throughput](results/reports/figures/pcap_throughput.png)

### Pcap Retransmissions
![Pcap Retransmissions](results/reports/figures/pcap_retransmissions.png)


## Data Export

All chart data is available in Excel format: `results/reports/chart_data.xlsx`

Sheets included:
- Latency_by_Scenario
- TTFT_by_Scenario
- Latency_Breakdown
- Throughput
- Bandwidth_Asymmetry
- Success_Rate
- Streaming_Metrics
- Token_Counts
- Latency_by_Profile
- Latency_Heatmap
- TTFT_Heatmap
- Raw_Data
