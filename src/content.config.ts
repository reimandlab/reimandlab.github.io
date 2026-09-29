import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const md = (dir: string) => glob({ pattern: '**/*.md', base: `./src/content/${dir}` });
const theme = z.enum(['drivers', 'multi-omics', 'biomarkers']);
export const newsTypes = ['paper', 'preprint', 'award', 'talk', 'people', 'update'] as const;

const people = defineCollection({
  loader: md('people'),
  schema: z.object({
    name: z.string(),
    role: z.enum(['pi', 'postdoc', 'staff', 'phd', 'msc', 'student', 'visitor']).optional(),
    status: z.enum(['current', 'alumni']).default('current'),
    title: z.string().optional(),        // overrides the role label
    affiliation: z.string().optional(),
    program: z.string().optional(),
    photo: z.string().optional(),        // path under public/, e.g. /images/people/name.jpg
    interest: z.string().optional(),     // one line
    years: z.string().optional(),        // e.g. "2019–2024" (alumni)
    now: z.string().optional(),          // current position (alumni)
    links: z.record(z.string().url()).optional(),
    author_names: z.array(z.string()).default([]), // other spellings used in author lists
    order: z.number().default(50),
  }),
});

const papers = defineCollection({
  loader: md('papers'),
  schema: z.object({
    title: z.string(),
    authors: z.array(z.string()).min(1),  // "Name*" marks co-first / co-corresponding
    authors_truncated: z.boolean().default(false), // list is incomplete; shown with "et al."
    journal: z.string(),
    year: z.number().int(),
    doi: z.string().optional(),
    pmid: z.coerce.string().optional(),
    url: z.string().url().optional(),
    preprint: z.string().url().optional(),
    code: z.string().url().optional(),
    type: z.enum(['article', 'preprint']).default('article'),
    themes: z.array(theme).default([]),
    featured: z.boolean().default(false),
    lab_led: z.boolean().optional(),      // leave out to infer from first/last author
  }),
});

const software = defineCollection({
  loader: md('software'),
  schema: z.object({
    name: z.string(),
    tagline: z.string(),
    order: z.number().default(50),
    themes: z.array(theme).default([]),
    image: z.string().optional(),
    links: z.record(z.string().url()).default({}),
    paper: z.string().optional(),         // DOI of the main paper
  }),
});

const research = defineCollection({
  loader: md('research'),
  schema: z.object({ title: z.string(), order: z.number(), icon: z.string().optional() }),
});

const posts = defineCollection({
  loader: md('posts'),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    type: z.enum(newsTypes),
    short: z.string(),                    // one-liner shown in the news feed
  }),
});

export const collections = { people, papers, software, research, posts };
