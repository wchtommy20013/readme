Database
===

Relational Database
---

- MySQL

Non-relational Database
---

### 1. Document data stores
- [CouchDB](./CouchDB/index.md) 
  - https://couchdb.apache.org/

### 2. Key/value data stores

### 3. Columnar data stores
    
### 4. Graph data stores

### 5. Time series data stores
- [InfluxDB]()
  - https://www.influxdata.com/

### 6. Object data stores

### 7. External index data stores


| Requirement                                  	| Document                                       	| Columnar                                                	| Key-Value            	| Graph                  	| Time Series    	| Object         	| External index  	|
|----------------------------------------------	|------------------------------------------------	|---------------------------------------------------------	|----------------------	|------------------------	|----------------	|----------------	|-----------------	|
| Normalization                                	| Denormalized                                   	| Denormalized                                            	| Denormalized         	| Normalized             	| Normalized     	| Denormalized   	| Denormalized    	|
| Schema                                       	| Schema on read                                 	| Column families defined on write, column schema on read 	| Schema on read       	| Schema on read         	| Schema on read 	| Schema on read 	| Schema on write 	|
| Consistency (across concurrent transactions) 	| Tunable consistency, document-level guarantees 	| Column-family–level guarantees                          	| Key-level guarantees 	| Graph-level guarantees 	|                	|                	|                 	|
|                                              	|                                                	|                                                         	|                      	|                        	|                	|                	|                 	|
|                                              	|                                                	|                                                         	|                      	|                        	|                	|                	|                 	|
You can now import Markdown table code directly using File/Paste table data... dialog.


Message Queuing
---

- [Kafka + ZooKeeper](./Kafka_Zookeeper/index.md)</a>
    - https://kafka.apache.org/
    - https://zookeeper.apache.org/