# Code Example

## TemplateDatabaseDAO.ts
```ts
import fetch = require('node-fetch');

export interface ITemplateDatabaseDAO {
    readonly endpoint: string;
    database: string;

    ping(): Promise<TemplateDatabaseActionResponse>;

    createdb(): Promise<TemplateDatabaseActionResponse>;
    deletedb(): Promise<TemplateDatabaseActionResponse>;

    list(): Promise<TemplateDatabaseActionResponse>
    listrevs(id: string): Promise<TemplateDatabaseActionResponse>

    find(id: string, rev?: string): Promise<TemplateDatabaseActionResponse>;
    findPlain(id: string, rev?: string): Promise<TemplateDatabaseActionResponse>;

    add(id: string, data: any): Promise<TemplateDatabaseActionResponse>;
    update(id: string, rev: string, data: any): Promise<TemplateDatabaseActionResponse>;
    archive(id: string, rev: string): Promise<TemplateDatabaseActionResponse>;
}

export interface TemplateDatabaseActionResponse {
    ok: boolean;
    error?: string;
    data?: any;
}

export interface IDocumentMeta {
    _id: string;
    _rev: string;
    author_: string;
    created_at_: string;
}

class DocumentMeta implements IDocumentMeta {
    public _id: string = '';
    public _rev: string = '';
    public author_: string = '';
    public created_at_: string = '';
}

export class TemplateDatabaseDAO implements ITemplateDatabaseDAO {
    public readonly endpoint: string;
    public database: string;

    public constructor(endpoint: string, database: string) {
        this.endpoint = endpoint;
        this.database = database;
    }

    public async ping(): Promise<TemplateDatabaseActionResponse> {
        return fetch.default(this.endpoint, {
            method: 'GET',
        }).then(response => {
            return response.json();
        }).then(data => {
            return {
                ok: data.ok || false,
                error: data.error,
                data: data
            }
        });
    }

    public async createdb(): Promise<TemplateDatabaseActionResponse> {
        return fetch.default(`${this.endpoint}/${this.database}`, {
            method: 'PUT',
        }).then(response => {
            return response.json();
        }).then(data => {
            return {
                ok: data.ok || false,
                error: data.error,
                data: data
            }
        });
    }

    public async deletedb(): Promise<TemplateDatabaseActionResponse> {
        return fetch.default(`${this.endpoint}/${this.database}`, {
            method: 'DELETE',
        }).then(response => {
            return response.json();
        }).then(data => {
            return {
                ok: data.ok || false,
                error: data.error,
                data: data
            }
        });
    }

    public async add(id: string, data: any, author: string = 'Unknown'): Promise<TemplateDatabaseActionResponse> {
        data._id = id;
        data.author_ = author;
        data.created_at_ = new Date().toISOString();
        return fetch.default(`${this.endpoint}/${this.database}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        }).then(response => {
            return response.json();
        }).then(data => {
            return {
                ok: data.ok || false,
                error: data.error,
                data: data
            }
        });
    }
    public async update(id: string, rev: string, data: any, author: string = 'Unknown'): Promise<TemplateDatabaseActionResponse> {
        data.author_ = author;
        data.created_at_ = new Date().toISOString();
        return fetch.default(`${this.endpoint}/${this.database}/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'If-Match': rev
            },
            body: JSON.stringify(data),
        }).then(response => {
            return response.json();
        }).then(data => {
            return {
                ok: data.ok || false,
                error: data.error,
                data: data
            }
        });
    }


    public async list(): Promise<TemplateDatabaseActionResponse> {
        return fetch.default(`${this.endpoint}/${this.database}/_all_docs`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
        }).then(response => {
            return response.json();
        }).then(data => {
            return {
                ok: data !== undefined && data.error === undefined,
                error: data.error,
                data: data
            }
        });
    }

    public async listrevs(id: string): Promise<TemplateDatabaseActionResponse> {
        return fetch.default(`${this.endpoint}/${this.database}/${id}?revs=true`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
        }).then(response => {
            return response.json();
        }).then(data => {
            return {
                ok: data !== undefined && data.error === undefined,
                error: data.error,
                data: data
            }
        });
    }

    public async find(id: string, rev?: string): Promise<TemplateDatabaseActionResponse> {
        let query = ''
        if (rev !== undefined) {
            query = `?rev=${rev}`
        }
        return fetch.default(`${this.endpoint}/${this.database}/${id}${query}`, {
            method: 'GET',
        }).then(response => {
            return response.json();
        }).then(data => {
            return {
                ok: data !== undefined && data.error === undefined,
                error: data.error,
                data: data
            }
        });
    }

    public async findPlain(id: string, rev?: string): Promise<TemplateDatabaseActionResponse> {
        let res = await this.find(id, rev);
        for (let metaKey of Object.keys(new DocumentMeta())) {
            delete res.data[metaKey];
        }
        return res;
    }

    public async archive(id: string, rev: string): Promise<TemplateDatabaseActionResponse> {
        return fetch.default(`${this.endpoint}/${this.database}/${id}`, {
            method: 'DELETE',
            headers: {
                'If-Match': rev
            }
        }).then(response => {
            return response.json();
        }).then(data => {
            return {
                ok: data !== undefined && data.error === undefined,
                error: data.error,
                data: data
            }
        });
    }
}
```

## test.ts
```ts
suite('Template Database Service', () => {
    const test_db = 'test';

    suite('Init', () => {

        test('T-I-001. Test CouchDB Connection', async () => {
            let db = new TemplateDatabaseDAO('http://localhost:5984', test_db);
            let res = await db.ping();
            expect(res).not.eq(undefined);
        });
        test('T-I-002. Create template database', async () => {
            let db = new TemplateDatabaseDAO('http://localhost:5984', test_db);
            let res = await db.createdb();
            expect(res.ok).eq(true);
        });
        test('T-I-003. Re-create template database', async () => {
            let db = new TemplateDatabaseDAO('http://localhost:5984', test_db);
            let res = await db.createdb();
            expect(res.ok).eq(false);
            expect(res.error).eq('file_exists');
        });
        test('T-I-004. Remove template database', async () => {
            let db = new TemplateDatabaseDAO('http://localhost:5984', test_db);
            let res = await db.deletedb();
            expect(res.ok).eq(true);
        });
    });

    suite('IO', () => {
        let db = new TemplateDatabaseDAO('http://localhost:5984', test_db);

        let data_fpath = path.join(__filename, '../Data');

        Mocha.before(async () => {
            await db.createdb();
        });



        test('T-IO-001. Add Document', async () => {
            let res = await db.add('Test', JSON.parse(fs.readFileSync(path.join(data_fpath, 'sample_import_template.json'), 'utf-8')));
            expect(res.ok).eq(true);
        });

        test('T-IO-002. Add Document with duplicated ID', async () => {
            let res = await db.add('Test', JSON.parse(fs.readFileSync(path.join(data_fpath, 'sample_import_template.json'), 'utf-8')));
            expect(res.ok).eq(false);
        });

        test('T-IO-003. List Document', async () => {
            let res = await db.list();
            expect(res.ok).eq(true);
            expect(res.data.total_rows).eq(1);
            expect(res.data.rows[0].id).eq('Test');
            expect(res.data.rows[0].key).eq('Test');
        });

        test('T-IO-004. Find Document', async () => {
            let res = await db.findPlain('Test');
            expect(res.ok).eq(true);
            assert.deepEqual(res.data, JSON.parse(fs.readFileSync(path.join(data_fpath, 'sample_import_template.json'), 'utf-8')));
        });

        test('T-IO-005. Update Document', async () => {
            let original = await db.find('Test');
            let orId = original.data._id;
            let orRev = original.data._rev;

            let res = await db.update(orId, orRev, {'Hello': 'World'});
            expect(res.ok).eq(true);

            let finalResult = await db.findPlain('Test');
            assert.deepEqual(finalResult.data, {'Hello': 'World'});
        });


        test('T-IO-006. List Document Revisions', async () => {
            let res = await db.listrevs('Test');
            expect(res.ok).eq(true);
            expect(res.data._id).eq('Test');
            expect(res.data._rev[0]).eq("2");
            expect(res.data._revisions.ids.length).eq(2);
            expect(res.data._revisions.start).eq(2);
        });

        test('T-IO-007. Archive Document', async () => {
            let original = await db.find('Test');
            let orId = original.data._id;
            let orRev = original.data._rev;

            let res = await db.archive(orId, orRev);
            expect(res.ok).eq(true);

            let deletesRes = await db.findPlain('Test');
            expect(deletesRes.ok).eq(false);
            expect(deletesRes.error).eq('not_found');
            expect(deletesRes.data.reason).eq('deleted');

            let reviveRes = await db.findPlain('Test', orRev);
            expect(reviveRes.ok).eq(true);
        });

        Mocha.after(async () => {
            await db.deletedb();
        });
    });
```