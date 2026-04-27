# TRACES

Run-level traces and sample request/response payloads.

## Selection Notes

- Data source: `logs/traffic_logs.db`
- Selection: latest fully successful session per scenario (fallback to latest session)
- Trace files are generated only when `TRACE_PAYLOADS=1` is set during runs.

## SDP Offer/Answer Samples (WebRTC)

Latest offer/answer pair captured during realtime WebRTC sessions for Realtime Audio WebRTC from `logs/sdp/`.

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

## Chat Basic

No records found for this scenario.

## Chat Streaming

No records found for this scenario.

## Realtime Text

No records found for this scenario.

## Realtime Audio

No records found for this scenario.

## Image Generation

No records found for this scenario.

## MCP Music Search

No records found for this scenario.

## Direct Web Search

No records found for this scenario.

## Computer Control

No records found for this scenario.
